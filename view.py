from os import listdir, system
from basics import *
from prettytable import PrettyTable


# ANSI Colors
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_CYAN = '\033[96m'
COLOR_WHITE_BG = "\033[47m"
COLOR_LIGHT_GRAY_BG = "\033[47;30m"
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
            elif line.startswith("<!p>"): # pragrahph end
                paragraph_in = False
            elif line.startswith("<p>") or paragraph_in: # paragraph start
                paragraph_in = True
                if line[3:].strip() == "":
                    continue
                if line.startswith("<p>"):
                    print(line[3:])
                else:
                    print(line)
            elif line.startswith("<!ta>"): # table end
                table_print(table_data)
                in_table = False
                table_data = []
            elif line.startswith("<ta>"): # table start
                in_table = True
            elif in_table:
                table_data.append([i.strip() for i in line.split(",")])
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
