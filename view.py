from os import name, system, listdir
from subprocess import CalledProcessError
try:
    from fuzzywuzzy import process
except ModuleNotFoundError:
    print("[!] Missing Module. Attempting to install it...")
    try:
        _ = system("pip install fuzzywuzzy")
        from fuzzywuzzy import process
    except CalledProcessError as e:
        print(f"[x] Failed to install 'fuzzywuzzy': {e}")
        print("[!] Please install 'fuzzywuzzy' manually and try running the program again.")
        exit()
try:
    from prettytable import PrettyTable
except ModuleNotFoundError:
    print("[!] Missing Module. Attempting to install it...")
    try:
        _ = system("pip install prettytable")
        from prettytable import PrettyTable
    except CalledProcessError as e:
        print(f"[x] Failed to install 'prettytable': {e}")
        print("[!] Please install 'prettytable' manually and try running the program again.")
        exit()
import inspect


AUTHOR = "Tousif Anaam"


class Menu():

    class ArgumentNotFuncError(Exception):
        pass

    def __init__(self, *args, validate_zero: bool = True, show_doc: bool = False) -> None:
        for i in args:
            if not inspect.isfunction(i):
                raise self.ArgumentNotFuncError(
                    "Only functions are checked as valid arguments.")
        self.funcs = args
        self.zero = validate_zero
        self.show_doc = show_doc

    def __str__(self):
        def f(x): return f"{(len(str(len(self.funcs))) - len(str(x))) * '0'}"
        res = "Options:\n"
        for x, i in enumerate(self.funcs):
            res += "[{0}{1}] {2}\n".format(f(x + 1), str(x + 1), i.__name__)
        return res


    def run(self, custom_str: str = None):
        clear()
        while True:
            if custom_str is not None and isinstance(custom_str, str):
                print(custom_str)
            else:
                print(self.__str__())
            foo = input("Choose an option: ").strip()
            print()

            # Try to convert input to integer
            try:
                option_index = int(foo)
                if 0 < option_index <= len(self.funcs):
                    self.funcs[option_index - 1]()
                    break
                elif self.zero and option_index == 0:
                    for func in self.funcs:
                        func()
                    break
            except ValueError:
                # Fuzzy search if input is not an integer
                matched_func, score = process.extractOne(
                    foo, [func.__name__ for func in self.funcs])
                if score >= 70:  # Adjust threshold as needed
                    for func in self.funcs:
                        if func.__name__ == matched_func:
                            func()
                            break
                    break

            clear()
            print("[!] INVALID OPTION SELECTED. ( No match found for '{0}' )\n".format(foo))


def clear() -> None:
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


# ANSI Colors
COLOR_BLACK = "\033[30m"
COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[33m'
COLOR_BLUE = '\033[34m'
COLOR_MAGENTA = '\033[35m'
COLOR_CYAN = '\033[36m'
COLOR_WHITE = '\033[37m'

COLOR_BLACK_BG = "\033[40m"
COLOR_RED_BG = '\033[41m'
COLOR_GREEN_BG = '\033[42m'
COLOR_YELLOW_BG = '\033[43m'
COLOR_BLUE_BG = '\033[44m'
COLOR_MAGENTA_BG = '\033[45m'
COLOR_CYAN_BG = '\033[46m'
COLOR_LIGHT_GRAY_BG = "\033[47m"
COLOR_DARK_GRAY_BG = "\033[100m"
COLOR_LIGHT_RED_BG = "\033[101m"
COLOR_LIGHT_GREEN_BG = "\033[102m"
COLOR_LIGHT_YELLOW_BG = "\033[103m"
COLOR_LIGHT_BLUE_BG = "\033[104m"
COLOR_LIGHT_MAGENTA_BG = "\033[105m"
COLOR_LIGHT_CYAN_BG = "\033[106m"
COLOR_WHITE_BG = "\033[107m"

COLOR_CLEAR_SCREEN = "\033[2J"
COLOR_RESET = '\033[0m'

def fileview(filename):

    def table_print(tab_data):
        table0 = PrettyTable(*[tab_data[0]])
        for i in tab_data[1:]:
            load = []
            for n in i:
                if n.startswith("%") and n.endswith("%"):
                    load.append(f"{COLOR_CYAN}{n[1:-1]}{COLOR_RESET}")
                else: load.append(n)
            table0.add_row(load)
        print(table0)

    def check_inline(line: str):
        line = line.replace("<c_bl>", f"{COLOR_BLACK}")
        line = line.replace("<c_r>", f"{COLOR_RED}")
        line = line.replace("<c_g>", f"{COLOR_GREEN}")
        line = line.replace("<c_y>", f"{COLOR_YELLOW}")
        line = line.replace("<c_b>", f"{COLOR_BLUE}")
        line = line.replace("<c_m>", f"{COLOR_MAGENTA}")
        line = line.replace("<c_c>", f"{COLOR_CYAN}")
        line = line.replace("<c_w>", f"{COLOR_WHITE}")
        line = line.replace("<cb_bl>", f"{COLOR_BLACK_BG}")
        line = line.replace("<cb_r>", f"{COLOR_RED_BG}")
        line = line.replace("<cb_g>", f"{COLOR_GREEN_BG}")
        line = line.replace("<cb_y>", f"{COLOR_YELLOW_BG}")
        line = line.replace("<cb_b>", f"{COLOR_BLUE_BG}")
        line = line.replace("<cb_m>", f"{COLOR_MAGENTA_BG}")
        line = line.replace("<cb_c>", f"{COLOR_CYAN_BG}")
        line = line.replace("<cb_lg>", f"{COLOR_LIGHT_GRAY_BG}")
        line = line.replace("<cb_dg>", f"{COLOR_DARK_GRAY_BG}")
        line = line.replace("<cb_lr>", f"{COLOR_LIGHT_RED_BG}")
        line = line.replace("<cb_lg>", f"{COLOR_LIGHT_GREEN_BG}")
        line = line.replace("<cb_ly>", f"{COLOR_LIGHT_YELLOW_BG}")
        line = line.replace("<cb_lb>", f"{COLOR_LIGHT_BLUE_BG}")
        line = line.replace("<cb_lm>", f"{COLOR_LIGHT_MAGENTA_BG}")
        line = line.replace("<cb_lc>", f"{COLOR_LIGHT_CYAN_BG}")
        line = line.replace("<cb_w>", f"{COLOR_WHITE_BG}")
        line = line.replace("<c_cs>", f"{COLOR_CLEAR_SCREEN}")
        line = line.replace("<c_rs>", f"{COLOR_RESET}")
        line = line.replace('<hi>', f"{COLOR_LIGHT_YELLOW_BG}{COLOR_BLACK}")
        line = line.replace('<!hi>', f"{COLOR_RESET}")
        return line

    clear() # clear screen
    with open(filename, "r+") as file:
        paragraph_in: bool = False
        table_data = []
        in_table: bool = False
        for line in file.readlines():
            if line.startswith("<title>"): # main title
                title = "TITLE: " + line[7:].upper().strip()
                print(f"\n{f'{COLOR_WHITE_BG}{COLOR_RED}Bismillahir Rahmanir Rahim{COLOR_RESET}'.center(100)}\n")
                print(f"{COLOR_BLUE}\n{title.center(100)}{COLOR_RESET}")
                print("-" * 100 + "\n\n")
            elif line.startswith("<t>"): # topic
                print(f"{COLOR_YELLOW}{' '.join(line[3:]).center(100)}{COLOR_RESET}\n")
            elif line.strip().startswith("-"): # bullet point
                bullet = line[:line.index('-')] + "• " + line[line.index('-') + 1:]
                print(f"{COLOR_GREEN}{bullet}{COLOR_RESET}")
            elif line.startswith("<i>"): # important
                print(f"{COLOR_RED}[ ♠ ] {line[3:]}{COLOR_RESET}")
            elif line.startswith("<e>"): # empty line
                print("\n")
            elif line.startswith("<h>"): # highlight
                print(f"{COLOR_LIGHT_GRAY_BG}{COLOR_BLUE} {COLOR_RED}{line[3:-1].strip()}{COLOR_RESET}")
            elif line.startswith("<w>"): # warning
                print(f"{COLOR_GREEN}{COLOR_YELLOW}  ⚠  {COLOR_GREEN} {COLOR_RED}{line[3:].strip()}{COLOR_RESET}")
            elif line.startswith("<sn>"): # self note
                "note not from lecture but for self as a reminder of something to be mindful."
                print(f"{COLOR_GREEN}{COLOR_YELLOW}  💡  {COLOR_GREEN} {COLOR_RED}{line[4:].strip()}{COLOR_RESET}")
            elif line.startswith("<!ta>"): # table end
                table_print(table_data)
                in_table = False
                table_data = []
            elif line.startswith("<ta>"): # table start
                in_table = True
            elif in_table:
                table_data.append([i.strip() for i in line.split(",")])
            elif line.startswith("<!p>"): # pragrahph end 
                paragraph_in = False
            elif line.startswith("<p>") or paragraph_in: # paragraph start
                paragraph_in = True
                if line[3:].strip() == "":
                    continue
                if line.startswith("<p>"):
                    print(check_inline(line[3:]))
                else:
                    print(check_inline(line))
            else:
                pass
    print("\n" + "-" * 100 + "\n\n")
    print(f"\n{f'{COLOR_WHITE_BG}{COLOR_RED}Alhamdulillah{COLOR_RESET}'.center(100)}\n")



load = []
for filename in listdir():
    if not filename.endswith(".py") and not filename.endswith(".bat") and not (filename.startswith("__") and filename.endswith("__")):
        exec(f"def {filename}():\n\tfileview('{filename}')")
        load.append(filename)

mymenu = Menu(*[eval(filename) for filename in load])
mymenu.run()
