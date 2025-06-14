from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt

from colorama import init, Fore
import sys, os, getpass, socket, wget, shutil, pathlib

# Version
ver = "3.0"


def clear():
    '''### Function to clear the console'''
    if os.name == "nt":
        os.system('cls')
    if os.name == "posix":
        os.system('clear')


if "--path:" in "".join(sys.argv):
    temp_path = ("".join(sys.argv[1:])).split("--path:")
    os.chdir(temp_path[-1])

if "--clear" in sys.argv or "-c" in sys.argv:
    clear()

# Decorative symbols
special = ["└", "┘", "┌", "┐", "├", "┤", "─", "│"]

# Path for service directories
modules_path = f"{pathlib.Path.home()}{os.sep}PyXe{os.sep}Modules"

# Checking for PyXe service directories in the user's home directory
if os.path.exists(f"{pathlib.Path.home()}{os.sep}PyXe") == False:
    os.mkdir(f"{pathlib.Path.home()}{os.sep}PyXe")
    os.mkdir(modules_path)

elif os.path.exists(modules_path) == False:
    os.mkdir(modules_path)
else:
    pass



init(autoreset=True)



if "--welcome" in sys.argv or "-w" in sys.argv:
    # Welcome message
    print(f"Welcome to PyXe command shell [{ver}]")
    print(f"""
    * Download:   {Fore.LIGHTBLUE_EX}https://github.com/Sp1kewall/PyXe/releases{Fore.RESET}

    * Modules:    {pathlib.Path.home()}{os.sep}PyXe{os.sep}Modules
    * History:    {pathlib.Path.home()}{os.sep}PyXe{os.sep}history.txt
    """)



def save_to_history(log: str):
    '''### Input history saving function'''
    if os.path.exists(
            f"{pathlib.Path.home()}{os.sep}PyXe{os.sep}history.txt"):
        with open(f"{pathlib.Path.home()}{os.sep}PyXe{os.sep}history.txt", "a", encoding="utf-8") as tmp_history_log:
            tmp_history_log.writelines(str(log) + "\n")
    else:
        with open(f"{pathlib.Path.home()}{os.sep}PyXe{os.sep}history.txt", "w", encoding="utf-8") as tmp_history_log:
            tmp_history_log.writelines(str(log) + "\n")


def new_good_path(path: str, part_of_path: str, new_root: str = "~") -> str:
    '''### Function to get a pretty path with home directory as tilde (~)'''
    tmp = path.replace(part_of_path, "")
    return f"{new_root}{tmp}"


def runfile(step_command: str, arguments: list = None):
    '''### Programs and modules launch function'''
    try:
        if os.path.exists(f"{modules_path}/{step_command}.py"):
            tmp_args = ""

            for i in range(len(arguments)):
                if arguments[i] == arguments[-1]:
                    tmp_args += f"{arguments[i]}"
                else:
                    tmp_args += f"{arguments[i]} "

            if os.name == "posix": os.system(f"python3 {modules_path}/{step_command}.py {tmp_args}")
            if os.name == "nt": os.system(f"{modules_path}/{step_command}.py {tmp_args}")
        else:
            print(step_command + " is not a command or an executable")
            print("Try to use help command to get more information")
            
    except BaseException:
        print(step_command + " is not a command or an executable")
        print("Try to use help command to get more information")

    print("")

# Dialog box for carbonate
save_dialog = input_dialog(
    title='Saving...',
    text='Please type filename:')

# Dialog box for carbonate
save_or_not = yes_no_dialog(
    title='Realy?',
    text='Do you want to save your file?')


def editor(filename: str = None):
    '''### Carbonate
    Build-in file editor'''
    class service:

        def bottom_toolbar_main():
            return HTML("| " + filename + '\n| Alt+Enter or Esc+Enter - Exit')

        def prompt_continuation(width, line_number, is_soft_wrap):
            return ' ' * width

        def clear():
            if os.name == "nt":
                os.system('cls')
            elif os.name == "posix":
                os.system("clear")
    try:
        service.clear()
        if os.path.isfile(filename):
            f = open(filename, 'r', encoding='utf-8')
            fff = f.read()
        else:
            fff = ''
        inp = prompt('', multiline=True, default='%s' % "".join(fff), prompt_continuation=service.prompt_continuation, bottom_toolbar=service.bottom_toolbar_main(), auto_suggest=AutoSuggestFromHistory())

        if ("%s" % inp) == fff:
            pass

        else:
            if save_or_not.run():
                if filename is None:
                    temp = open(save_dialog.run(), 'w', encoding='utf-8')
                    temp.writelines("%s" % inp)
                    temp.close()

                else:
                    temp = open(filename, 'w', encoding='utf-8')
                    temp.writelines("%s" % inp)
                    temp.close()

            else:
                pass
    except PermissionError:
        message_dialog(
            title='Permission Error',
            text='"Carbonate" does not have sufficient rights to create rights in this location\nor edit the selected file').run()

    except UnicodeDecodeError:
        message_dialog(
            title='UnicodeDecode Error',
            text='"Carbonate" cannot recognize the Unicode in the file, therefore cannot open or edit it').run()
    except KeyboardInterrupt:
        pass

# PyXe main code
while True:
    try:
        current_path = os.getcwd()
        if os.getcwd() == f"{pathlib.Path.home()}":
            current_path = "~"
        elif f"{pathlib.Path.home()}" in os.getcwd():
            # Console cursor (home directory)
            current_path = new_good_path(path=os.getcwd(), part_of_path=f"{pathlib.Path.home()}", new_root="~")

        # Console cursor
        cursor = ("[" + Fore.LIGHTBLACK_EX + getpass.getuser() + Fore.RESET + ":" + Fore.LIGHTBLACK_EX + socket.gethostname() + Fore.RESET + "]" + Fore.YELLOW + " " + current_path + Fore.RESET + " $: ")
        
        if len(cursor) > 100:
            cursor = ("[" + Fore.LIGHTBLACK_EX + getpass.getuser() + Fore.RESET + ":" + Fore.LIGHTBLACK_EX + socket.gethostname() + Fore.RESET + "]" + Fore.YELLOW + " " + current_path + Fore.RESET + "\n$: ")
        
        # Main input function
        user = input(cursor)

        # Splitting the entered data into a command and arguments
        tmp = user.split(" ")
        lex = tmp[0] #   Command
        arg = tmp[1::] # Arguments

        tmp_output = ' '.join(str(x) for x in arg) # Arguments too
        
        save_to_history(log=(user))

        if lex.lower() == 'help':
            if len(arg) == 0:
                print("\nTo get a list of third-party commands, type help -m or help --modules")
                print("\n<HELP     > list commands")
                print("<SAY      > output some text")
                print("<CLEAR    > clear screen")
                print("<LS       > view the contents of the current directory")
                print("<WIA      > view the path to the current directory")
                print("<CD       > change directory")
                print("<MKDIR    > create a directory")
                print("<RMDIR    > delete directory")
                print("<RM       > delete selected file")
                print("<FILE     > open text editor")
                print("<TOUCH    > create file without editing")
                print("<CAT      > output the contents of the file")
                print("<CP       > copy the file to some location or file")
                print('<WGET     > download file from internet')
                print("<DOC      > read the documentation for any command not included in the standard set")
                print("<VER      > view shell version\n")

            elif arg[0].lower() == "--help":
                print("HELP - Command for getting information about a command from the standard set or a list of all commands from the standard set\nTo get a list of third-party commands, type help -m or help --modules\n\n")

            elif arg[0].lower() == '--say':
                print("SAY - Command for displaying text/math on the screen\nSpecify text or mathematical action as an argument\n\n")
            elif arg[0].lower() == '--clear':
                print("CLEAR - Command to clear the screen\n\n")
            elif arg[0].lower() == '--ls':
                print("LS - Command to view the contents of a directory.\nIf the object's font is grey, then it is a directory. If white - file\n\n")
            elif arg[0].lower() == '--wia':
                print("WIA - Command to display the current path\n\n")
            elif arg[0].lower() == '--cd':
                print("CD - Command to change directory\nDirectory name as an argument\n\n")
            elif arg[0].lower() == '--crctl':
                print("MKDIR - Command to create a directory\nDirectory name as an argument\n\n")
            elif arg[0].lower() == '--rmctl':
                print("RMDIR - Command to remove a directory\nDirectory name as an argument\n\n")
            elif arg[0].lower() == '--rm':
                print("RM - Command to delete a file\nThe file name is given as an argument")
            elif arg[0].lower() == '--file':
                print("FILE - Command to open a text editor (on macOS and Linux it's nano, on Windows it's a built-in editor)\nThe file name is given as an argument\n\n")
            elif arg[0].lower() == '--touch':
                print("TOUCH - Command to create a file without editing\nThe file name is given as an argument\n\n")
            elif arg[0].lower() == '--cat':
                print("CAT - Command to display the contents of a file\nThe file name is given as an argument\n\n")
            elif arg[0].lower() == "--ver":
                print("VER - Command to display version information\n\n")
            elif arg[0].lower() == '--cp':
                print("CP - Command for copying a file from one directory to another (if a file is specified in the second argument, then the contents of the first argument will be copied to it)\nSpecify the file to be copied as the first argument. Specify the final path in the second argument\n\n")
            elif arg[0].lower() == '--wget':
                print("WGET - Command to download a file from the Internet\nSpecify the download link in the argument\n\n")
            elif arg[0].lower() == "--doc":
                print("DOC - Command to get information about a module for the shell. The documentation file looks like this: \"doc_{module name without spaces}.txt\"\n\n")

            elif arg[0].lower() == '--modules' or arg[0].lower() == '-m':

                # View available modules
                print("\n", end="")

                for i in os.listdir(modules_path):
                    tmp_filename = i.split(".")
                    if len(tmp_filename) > 1 and tmp_filename[1] == "py" and " " not in tmp_filename[0]:
                        print(tmp_filename[0])

                print("\n", end="")

            else:
                print("\nTo get a list of third-party commands, type help -m or help --modules")
                print("\n<HELP     > list commands")
                print("<SAY      > output some text")
                print("<CLEAR    > clear screen")
                print("<LS       > view the contents of the current directory")
                print("<WIA      > view the path to the current directory")
                print("<CD       > change directory")
                print("<MKDIR    > create a directory")
                print("<RMDIR    > delete directory")
                print("<RM       > delete selected file")
                print("<FILE     > open text editor")
                print("<TOUCH    > create file without editing")
                print("<CAT      > output the contents of the file")
                print("<CP       > copy the file to some location or file")
                print('<WGET     > download file from internet')
                print("<DOC      > read the documentation for any command not included in the standard set")
                print("<VER      > view shell version\n")

        elif lex.lower() == 'say':
            try:
                if len(arg) == 0:
                    print("Bad argument\nUse help --say to get more information")
                else:

                    try:
                        print(eval(tmp_output))
                    except SyntaxError:
                        print(tmp_output)
                    except ZeroDivisionError:
                        print("Can't divide by zero")
                        print("Use help --say to get more information")
                    except NameError:
                        print(tmp_output)
            except IndexError:
                print("Bad argument\nUse help --say to get more information")
            print("")

        elif lex.lower() == "clear":
            clear()

        elif lex.lower() == 'ls':
            print("")
            try:
                if len(os.listdir(".")) < 1:
                    print("Directory is empty")

                print((special[6] * 8) + special[3])
                for i in os.listdir("."):
                    if os.path.isdir(i):
                        print("\t" + special[4], Fore.LIGHTBLACK_EX + i)
                    else:
                        print("\t" + special[4], Fore.RESET + i)
                print((special[6] * 8) + special[1])

            except PermissionError:
                print('I was denied access')
                print("You can run me as ROOT (sudo)")

            print("")

        elif lex.lower() == 'wia':
            print(os.getcwd())
            print("")

        elif lex.lower() == 'cd':
            if len(arg) == 0:
                print("Bad directory name")
                print('Use help --cd to get more information')
            else:
                tmp_output0 = tmp_output.replace(
                    "~", f"{pathlib.Path.home()}")

                try:
                    os.chdir(tmp_output0)

                except FileNotFoundError:
                    print(f"Directory {tmp_output} not found")
                    print('Use help --cd to get more information')
                except NotADirectoryError:
                    print(tmp_output + " is not a directory")
                    print('Use help --cd to get more information')

        elif lex.lower() == 'mkdir':
            if len(arg) == 0:
                print("Bad directory name")
                print("Use help --mkdir to get more information")
            else:
                arg[0] = arg[0].replace("~", f"{pathlib.Path.home()}")
                try:
                    arg[0] = arg[0].replace("/", os.sep)

                    CoolPath = arg[0].split(os.sep)

                    none = ""

                    for j in CoolPath:
                        if os.path.exists(none + j):
                            none += f"{j}/"
                        
                        else:
                            os.mkdir(none + j)
                            none += f"{j}/"


                except OSError:
                    print(f"Directory cannot be named {tmp_output}")
                    print('Use help --mkdir to get more information')
            print("")

        elif lex.lower() == 'rmdir':
            if len(arg) == 0:
                print("Bad directory name")
                print("Use help --rmdir to get more information")
            else:

                try:
                    shutil.rmtree(tmp_output)
                except FileNotFoundError:
                    print(f"Directory {arg} not found")
                    print('Use help --rmdir to get more information')
                except OSError:
                    print(f"Directory cannot be named {tmp_output}")
                    print('Use help --rmdir to get more information')
            print("")

        elif lex.lower() == 'file':
            if len(arg) == 0:
                print("Bad filename")
                print('Use help --file to get more information')
            else:

                editor(tmp_output)
            clear()

        elif lex.lower() == 'cat':
            if len(arg) == 0:
                print("Bad filename")
                print('Use help --cat to get more information')
            else:

                if os.path.isfile(tmp_output):
                    try:
                        f = open(tmp_output, 'r', encoding="utf-8")
                        print(f.read())
                        f.close()
                    except UnicodeDecodeError:
                        print(f"File {tmp_output} cannot be found, read or edited")
                        print('Use help --cat to get more information')
                    except FileNotFoundError:
                        print(f"File {tmp_output} not found")
                        print('Use help --cat to get more information')
                else:
                    print(f"{tmp_output} is not file")
                    print('Use help --cat to get more information')
            print("")

        elif lex.lower() == 'rm':
            if len(arg) == 0:
                print("Bad filename")
                print('Use help --rm to get more information')
                print("")

            else:
                if tmp_output != os.path.basename(__file__):
                    try:
                        os.remove(tmp_output)
                    except FileNotFoundError:
                        print(f"File {tmp_output} not found")
                        print('Use help --rm to get more information')
                        print("")
                else:
                    print("You can't delete me >:(") # Please do not attempt to remove the PyXe
                    print("")

        elif lex.lower() == "ver":
            print(ver)
            print("")

        elif lex.lower() == "touch":
            if len(arg) == 0:
                print("Bad filename")
                print('Use help --touch to get more information')
                print("")
            else:

                try:
                    with open(tmp_output, 'w') as lol1:
                        lol1.close()
                except FileNotFoundError:
                    print(f"File {tmp_output} not found")
                    print("")

        elif lex.lower() == "cp":
            if len(arg) == 0:
                print("Bad filename")
                print('Use help --cp to get more information')
                print("")
            else:
                try:
                    shutil.copy2(arg[0], arg[1])
                except FileNotFoundError:
                    print(f"I can't found {arg[0]} or {arg[1]}")
                    print("")
                except IndexError:
                    print("Not enough arguments!")
                    print("")
                except PermissionError:
                    try:
                        shutil.copytree(arg[0], arg[1])
                    except BaseException:
                        print("I cannot move this object")
                        print("")

        elif lex.lower() == "wget":
            if len(arg) == 0:
                print("Bad URL")
                print('Use help --wget to get more information')
            else:
                print("Trying to download a file...\n")
                try:
                    wget.download(tmp_output)
                    print("\nFile downloaded!\n")
                except BaseException:
                    print("\nFailed to download file. Maybe it's damaged or you don't have an internet connection\n")
                    
            print("")

        elif lex.lower() == "doc":
            if len(arg) > 0:
                try:

                    f = open(
                        f"{modules_path}/doc_{arg[0]}.txt", 'r', encoding="utf-8")
                    print(f.read())
                    f.close()

                except BaseException:
                    print("Error when reading the documentation")

            print("")

        elif lex.lower() == "login":
            print(getpass.getuser())

        elif lex.lower() == "host":
            print(socket.gethostname())

        elif lex.lower() == 'exit':
            print("Exit...\n\n")
            sys.exit()

        else:
            try:
                runfile(lex, arg)
            except NameError:
                if len(arg) == 0:
                    pass
                else:
                    print(f"Name error. Perhaps when trying to open a supposed file called {arg}, PyXe was horrified because this file was not found")

            except BaseException:
                print('An unknown error has occurred :/')

    except KeyboardInterrupt:
        print("\nExit...\n\n")
        exit()


    except PermissionError:
        print("Permission denied")