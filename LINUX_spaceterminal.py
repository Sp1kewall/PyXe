import os, sys, lib_platform
from os import path
from colorama import init, Fore
from colorama import Back
from pyqadmin import admin 
from colorama import Style
from pathlib import Path
os.system("title Space Terminal")
os.system("sudo -s")
init(autoreset=True)
cursor = (Fore.GREEN + lib_platform.username + Fore.CYAN + "%" + Fore.RED + lib_platform.hostname + Fore.BLUE + ' ~' + Fore.WHITE + '$:')
#                                                                                                                            ================
#                                                                                                                            Hello from 2022!
#                                                                                                                            ================ 
os.chdir(lib_platform.path_userhome)
os.system(command='clear')
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
        os.system(command='clear')

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
        os.system("nano " + arg)

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
                os.startfile(user)
            except:
                pass
        except:
            print(user + " is not a command or file")
while True:
    user = input(cursor)
    if lexer(user): break