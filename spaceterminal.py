import os, sys, lib_platform
from os import path
from colorama import init, Fore
from colorama import Back
from pyqadmin import admin 
from colorama import Style
from pathlib import Path
os.system("title Space Terminal")
init(autoreset=True)
cursor = (Fore.GREEN + lib_platform.username + Fore.CYAN + "%" + Fore.RED + lib_platform.hostname + Fore.BLUE + ' ~' + Fore.WHITE + '$:')
#                                                                                                                            ================
#                                                                                                                            Hello from 2022!
#                                                                                                                            ================ 
os.chdir(lib_platform.path_userhome)
os.system(command='cls')
print("""Space Terminal
Made by """ + Fore.YELLOW + """Space Core""" + Fore.WHITE + """
My Discord          --> Space Core#8097
My Steam            --> 1144347594
Enter the HELP command to get the command sheet\n\n""")
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
def shell(lex,arg):
    if lex == 'help' or lex == 'HELP':
        print("<HELP     > get a list of commands")
        print("<SAY      > output anything text")
        print("<CLEAR    > clear screen")
        print("<LS       > view the current directory")
        print("<WIA      > display the path to the current directory")
        print("<CD       > change the current directory")
        print("<CRCTL    > create folder")
        print("<RMCTL    > remove folder")
        print("<RM       > delete the selected file")
        print("<FILE     > open the text editor")
        print("<TYPE     > display the contents of the file")
    elif lex == 'say' or lex == 'SAY':
        print(arg)

    elif lex == 'ls' or lex == 'LS':
        rez = sorted(os.listdir("."))
        for n, item in enumerate(rez):
            print(n+1, item)

    elif lex == 'wia' or lex == 'WIA':
        print(os.getcwd())
    elif lex == 'clear' or lex == 'CLEAR':
        os.system(command='cls')

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
                print("Directory " + arg + "does not exist")
            except OSError:
                print("Directory cannot be named " + arg)
    elif lex == 'file' or lex == 'FILE':
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
    elif lex == 'type' or lex == 'TYPE':
        try:
            f = open(arg, 'r')
            print(f.read())
            f.close()
        except UnicodeDecodeError:
            print("Unable to read file")
    elif lex == '':
        pass
    elif lex == 'rm' or lex == 'RM':
            try:
                os.remove(arg)
            except FileNotFoundError:
                print("File " + arg + "no found")
    else:
        try:
            try:
                os.startfile(user + '.bat')
            except:
                try:
                    os.startfile(user + '.exe')
                except:
                    pass
        except:
            print(user + " is not a command, batch/executable file")
while True:
    user = input(cursor)
    if lexer(user): break