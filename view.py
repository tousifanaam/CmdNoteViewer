from os import listdir, system
from basics import Menu

# Define ANSI color escape codes
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_CYAN = '\033[96m'
COLOR_WHITE_BG = "\033[47m"
COLOR_CLEAR_SCREEN = "\033[2J"
COLOR_RESET = '\033[0m'  # Reset to default color

def fileview(filename):
    _ = system('cls')  # Clear screen (Windows)
    with open(filename, "r+") as file:
        paragraph_in: bool = False
        for line in file.readlines():
            if line.startswith("<title>"):
                title = "TITLE: " + line[7:].upper().strip()
                print(f"\n{f'{COLOR_WHITE_BG}{COLOR_RED}Bismillahir Rahmanir Rahim{COLOR_RESET}'.center(100)}\n")
                print(f"{COLOR_BLUE}\n{title.center(100)}{COLOR_RESET}")
                print("-" * 100 + "\n\n")
            elif line.startswith("<t>"):
                print(f"{COLOR_YELLOW}{' '.join(line[3:]).center(100)}{COLOR_RESET}\n")
            elif line.strip().startswith("-"):
                bullet = line[:line.index('-')] + "• " + line[line.index('-') + 1:]
                print(f"{COLOR_GREEN}{bullet}{COLOR_RESET}")
            elif line.startswith("<i>"):
                print(f"{COLOR_RED}[ ♠ ] {line[3:]}{COLOR_RESET}")
            elif line.startswith("<!p>"):
                paragraph_in = False
            elif line.startswith("<p>") or paragraph_in:
                paragraph_in = True
                if line[3:].strip() == "":
                    continue
                if line.startswith("<p>"):
                    print(line[3:])
                else:
                    print(line)
            elif line.startswith("<e>"):
                print("\n")
            else:
                pass
    print("-" * 100 + "\n\n")
    print(f"\n{f'{COLOR_WHITE_BG}{COLOR_RED}Alhamdulillah{COLOR_RESET}'.center(100)}\n")



load = []
for filename in listdir():
    if not filename.endswith(".py") and not filename.endswith(".bat"):
        exec(f"def {filename}():\n\tfileview('{filename}')")
        load.append(filename)

mymenu = Menu(*[eval(filename) for filename in load])
mymenu.run()
