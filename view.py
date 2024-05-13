from os import listdir, system
from basics import *
from prettytable import PrettyTable


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
        # add colors
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
        if '<hi>' in line:
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
    if not filename.endswith(".py") and not filename.endswith(".bat"):
        exec(f"def {filename}():\n\tfileview('{filename}')")
        load.append(filename)

mymenu = Menu(*[eval(filename) for filename in load])
mymenu.run()
