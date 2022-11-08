#==========================================================================================================================
import os, sys, time
from os import path
from os import name
def clear():
    c = 'clear'
    if name == 'nt': c = 'cls'
    os.system(c)
try:
    import lib_platform
    from colorama import init, Fore
    from colorama import Back
    from pyqadmin import admin 
    from colorama import Style
    from pathlib import Path
except:
    ask_true = True
    while ask_true:
        clear()
        ask = input("""
Oh no! It looks like one of the required
modules is not installed for your Python! We
strongly recommend installing each of these
modules, but you can proceed at your own
risk. Install modules?
[y/n] $:""")
    if ask == 'y' or ask == 'Y':
        ask_true = False
        if name == 'nt':
            os.system("pip install lib_platform")
            os.system("pip install pyqadmin")
            os.system("pip install colorama")
        elif name == 'posix':
            os.system("sudo apt install python3-pip")
            os.system("pip install lib_platform")
            os.system("pip install pyqadmin")
            os.system("pip install colorama")
        clear()
        print("After 3 seconds Space Terminal will shut down automatically")
        time.sleep(3)
        sys.exit()
    elif ask == 'n' or ask == 'N':
        ask_true = False
        pass
    else:
        pass
#==========================================================================================================================

def runfile(x):
    if name == 'nt':
        try:
            os.startfile(x + '.bat')
        except:
            try:
                os.startfile(x + '.exe')
            except:
                print(x + " is not a command or executable file")
    elif name == 'posix':
        try:
            os.startfile(x)
        except:
            print(x + " is not a command or executable file")
def file(arg):
    if name == 'nt':
            try:
                file_path = arg
                if path.exists(file_path):
                    print("\n\tFile already exists!")
                    ans = input("\nDo you want to use this file? (y/n)\n$:")
                    if ans == 'y' or ans == 'Y':
                        file = open(file_path, "a")
                        ans = input("\nDo you want to erase all content? (y/n)\n$:")
                        if ans == 'y' or ans == 'Y':
                            print("\n\tErasing...\n")
                            file.seek(0)
                            file.truncate()
                        else:
                            pass
                        
                    else:
                        exit()
                else:
                    print("\n\tCreating new file...\n")
                    file = open(file_path, "a")
                print("\nPress RETURN to start a new line.\nPress Ctrl + C to save and close.\n\n")
                line_count = 1
                while line_count > 0:
                    try: 
                        line = input("\t" + str(line_count) + " ")
                        file.write(line)
                        file.write('\n')
                        line_count += 1
                    except KeyboardInterrupt:
                        print("\n\n\tClosing...")
                        break
                    
                file.close()
            except FileNotFoundError:
                    print("The " + arg + " file was not found or could not be created")


    elif name == 'posix':
        os.system("nano " + arg)
#==========================================================================================================================
os.system("title Space Terminal")
init(autoreset=True)
cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "%" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' ~' + Fore.WHITE + '$:')

os.chdir(lib_platform.path_userhome)
clear()
print("""Space Terminal
Made by """ + Fore.YELLOW + """Space Core""" + Fore.WHITE + """
My Discord          --> Space Core#8097
My Steam            --> 1144347594
Enter the HELP command to get the command sheet\n\n""")
#==========================================================================================================================
def lexer(c):
    lex=''
    arg=''
    l=True 
    for i in c:
        if i==' ' and l:
            l=False
        elif l:
            lex+=i
        else:
            arg+=i
    return shell(lex,arg)
#==========================================================================================================================
def shell(lex,arg):

    if lex == 'help' or lex == 'HELP':
        print("<HELP     > get a list of commands")
        print("<SAY      > output anything text")
        print("<CLEAR    > clear screen")
        print("<LS       > view the current directory")
        print("<WIA      > display the path to the current directory")
        print("<CD       > change the current directory")
        print("<CRCTL    > create directory")
        print("<RMCTL    > remove directory")
        print("<RM       > delete the selected file")
        print("<FILE     > open the text editor")
        print("<TOUCH    > creates a file without editing")
        print("<CAT      > display the contents of the file")
        print("<VER      > view terminal version")
    elif lex == 'say' or lex == 'SAY':
        print(arg)

    elif lex == 'ls' or lex == 'LS':
        rez = sorted(os.listdir("."))
        for n, item in enumerate(rez):
            print(n+1, item)

    elif lex == 'wia' or lex == 'WIA':
        print(os.getcwd())
    elif lex == 'clear' or lex == 'CLEAR':
        clear()

    elif lex == 'cd' or lex == 'CD':
            try:
                os.chdir(arg)
            except FileNotFoundError:
                print("Directory " + arg + " not found")
            except OSError:
                print("An unexpected error has occurred :/")

    elif lex == 'crctl' or lex == 'CRCTL':
        try:
            os.mkdir(arg)
        except OSError:
            print("Directory cannot be named " + arg)
    elif lex == 'rmctl' or lex == 'RMCTL':
            try:
                os.rmdir(arg)
            except FileNotFoundError:
                print("Directory " + arg + " does not exist")
            except OSError:
                print("Directory cannot be named " + arg)
    elif lex == 'file' or lex == 'FILE':
        file(arg)
    elif lex == 'cat' or lex == 'CAT':
        try:
            f = open(arg, 'r')
            print(f.read())
            f.close()
        except UnicodeDecodeError:
            print("File " + arg + " unable to read")
    elif lex == '':
        pass
    elif lex == 'rm' or lex == 'RM':
            try:
                os.remove(arg)
            except FileNotFoundError:
                print("File " + arg + " no found")

    elif lex == 'user' or lex == 'USER':
        print(Fore.GREEN + lib_platform.username)

    elif lex == 'host' or lex == 'HOST':
        print(Fore.RED + lib_platform.hostname)
    
    elif lex == 'touch' or lex == 'TOUCH':
        with open(arg, 'w') as lol:
            lol.close()

    elif lex == 'cname' or lex == 'CNAME':
        if name == 'nt':
            print("Windows")
        elif lex == 'posix':
            print("Linux")

    elif lex == 'ver' or lex == 'VER':
        print("""
    Space Terminal
    Made by Space Core
    
    ====================
    Terminal version 1.3""")

    elif lex == 'exit' or lex == 'EXIT':
        print("Exit...\n\n\n")
        sys.exit()

    else:
        runfile(user)
#==========================================================================================================================
while True:
    user = input(cursor)
    if lexer(user): break



#==========================================================================================================================
