from os import listdir, system
from basics import Menu


def fileview(filename):
    _ = system('cls')
    with open(filename, "r+") as file:
        paragraph_in: bool = False
        for i in file.readlines():
            if i.startswith("<title>"): # for title or main heading <title>
                print(("TITLE: "+ i[7:].upper()).center(100))
                print(''.join(['-' for i in ("TITLE: "+ i[7:].upper()).center(100)]) + "\n\n")
            elif i.startswith("<t>"): # for topic <t>
                print((" ".join(i[3:]) + "\n\n").center(100))
            elif i.strip().startswith("-"): # for bullet points "-"
                print(i[:i.index('-')] + "• " + i[i.index('-') + 1:])
            elif i.startswith("<i>"): # important information
                print("[ ♠ ] " + i[3:])
            elif i.startswith("<!p>"): # paragraph end <!p>
                paragraph_in = False
            elif i.startswith("<p>") or paragraph_in: # paragraph start <p>
                paragraph_in = True
                if i[3:].strip() == "": continue
                if i.startswith("<p>"): print(i[3:])
                else: print(i)
            elif i.startswith("<e>"): # empty line <e>
                print("\n")
            else:
                pass


load = []
for i in listdir():
    if not i.endswith(".py") and not i.endswith(".bat"):
        exec(f"def {i}():\n\tfileview('{i}')")
        load.append(i)

mymenu = Menu(*[eval(i) for i in load])
mymenu.run()
