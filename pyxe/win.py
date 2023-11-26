ver = "2.8"
print("PyXe ver - " + ver)
import os, sys
import lib_platform

from colorama import init, Fore
import wget
import shutil

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML


special = ["└", "┘", "┌", "┐", "├", "┤", "─", "│"]

while True:
    try:
        def clear():
            os.system('cls')

        def runfile(x):
            try:
                os.startfile(x)
            except:
                print("")
                print(x + " is not a command or an executable")
                print("Try to use help command to get more information")
                print("")


        def file(arg):
            filename = arg
            try:
                clear()
                if os.path.isfile(filename):
                    f = open(filename, 'r', encoding='utf-8')
                    fff = f.read()
                else:
                    fff = ''
                inp = prompt('~ ', multiline=True, default='%s' % "".join(fff), prompt_continuation=prompt_continuation, bottom_toolbar=bottom_toolbar(filename))

                if ("%s" % inp) == fff:
                    pass
                else:
                    save = input("\n\nSave file?\n (y/n)> ")
                    if save == 'y':
                        fl = open(filename, 'w', encoding='utf-8')
                        fl.writelines("%s" % inp)
                        fl.close()
                    elif save == 'n':
                        pass
            except PermissionError:
                print("[ALERT] - Bad file path")

            except UnicodeDecodeError:
                print("[ALERT] - Bad unicode")
            except FileNotFoundError:
                    print("File " + arg + " cannot be found or edited")
                
        def bottom_toolbar(filename):
            return HTML(filename + ' | Alt+Enter or Esc+Enter - Exit')

        def prompt_continuation(width, line_number, is_soft_wrap):
            return ' ' * width

        init(autoreset=True)

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

            if lex.lower() == 'help':
                if arg.lower() == '--say':
                    print("SAY - Command for displaying text/math on the screen\nSpecify text or mathematical action as an argument\n\n")
                elif arg.lower() == '--clear':
                    print("CLEAR - Command to clear the screen\n\n")
                elif arg.lower() == '--ls':
                    print("LS - Command to view the contents of a directory.\nIf the object's font is green, then it is a directory. If blue - file\n\n")
                elif arg.lower() == '--wia':
                    print("WIA - Command to display the current path\n\n")
                elif arg.lower() == '--cd':
                    print("CD - Command to change directory\nDirectory name as an argument\n\n")
                elif arg.lower() == '--crctl':
                    print("MKDIR - Command to create a directory\nDirectory name as an argument\n\n")
                elif arg.lower() == '--rmctl':
                    print("RMDIR - Command to remove a directory\nDirectory name as an argument\n\n")
                elif arg.lower() == '--rm':
                    print("RM - Command to delete a file\nThe file name is given as an argument")
                elif arg.lower() == '--file':
                    print("FILE - Command to open a text editor (on macOS and Linux it's nano, on Windows it's a built-in editor)\nThe file name is given as an argument\n\n")
                elif arg.lower() == '--touch':
                    print("TOUCH - Command to create a file without editing\nThe file name is given as an argument\n\n")
                elif arg.lower() == '--cat':
                    print("CAT - Command to display the contents of a file\nThe file name is given as an argument\n\n")
                elif arg.lower() == "--ver":
                    print("VER - Command to display version information\n\n")
                elif arg.lower() == '--cp':
                    print("CP - Command for copying a file from one directory to another (if a file is specified in the second argument, then the contents of the first argument will be copied to it)\nSpecify the file to be copied as the first argument. Specify the final path in the second argument\n\n")
                elif arg.lower() == '--wget':
                    print("WGET - Command to download a file from the Internet\nSpecify the download link in the argument\n\n")
                else:
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
                    print("<VER      > view terminal version\n")


            elif lex.lower() == 'say':
                if arg == "":
                    print("")
                    print("Bad argument\nUse help --say to get more information")
                    print("")
                else:
                    try:
                        print(eval(arg))
                    except SyntaxError:
                        print(arg)
                    except ZeroDivisionError:
                        print("")
                        print("Can't divide by zero")
                        print("Use help --say to get more information")
                        print("")
                    except NameError:
                        print(arg)

            elif lex.lower() == 'ls':
                try:
                    print("")
                    print((special[6]*8) + special[3])
                    for i in os.listdir("."):
                            if os.path.isdir(i):
                                print("\t" + special[4], Fore.GREEN + i)
                            else:
                                print("\t" + special[4], Fore.BLUE + i)
                    print("")
                except PermissionError:
                    print('I was denied access')
                    print("You can run me as ROOT (sudo)")

            elif lex.lower() == 'wia':
                print(os.getcwd())
            elif lex.lower() == 'clear':
                clear()

            elif lex.lower() == 'cd':
                    if arg == "":
                        print("")
                        print("Bad directory name")
                        print('Use help --cd to get more information')
                        print("")
                    else:
                        if arg == '~':
                            os.chdir(lib_platform.path_userhome)
                        else:
                            try:
                                os.chdir(arg)
                            except FileNotFoundError:
                                print("")
                                print("Directory " + arg + " not found")
                                print('Use help --cd to get more information')
                                print("")
                            except NotADirectoryError:
                                print("")
                                print(arg + " is not a directory")
                                print('Use help --cd to get more information')
                                print("")

            elif lex.lower() == 'mkdir':
                if arg == '':
                    print("")
                    print("Bad directory name")
                    print("Use help --mkdir to get more information")
                    print("")
                else:
                    try:
                        os.mkdir(arg)
                    except OSError:
                        print("Directory cannot be named " + arg)
                        print('Use help --mkdir to get more information')
            elif lex.lower() == 'rmdir':
                    if arg == '':
                        print("")
                        print("Bad directory name")
                        print("Use help --rmdir to get more information")
                        print("")
                    else:
                        try:
                            shutil.rmtree(arg)
                        except FileNotFoundError:
                            print("")
                            print("Directory " + arg + " not found")
                            print('Use help --rmdir to get more information')
                            print("")
                        except OSError:
                                print("")
                                print("Directory cannot be named " + arg)
                                print('Use help --rmdir to get more information')
                                print("")

            elif lex.lower() == 'file':
                if arg == "":
                    print("")
                    print("Bad filename")
                    print('Use help --file to get more information')
                    print("")
                else:
                    file(arg)
            elif lex.lower() == 'cat':
                if arg == "":
                    print("")
                    print("Bad filename")
                    print('Use help --cat to get more information')
                    print("")
                else:
                    try:
                        f = open(arg, 'r')
                        print(f.read())
                        f.close()
                    except UnicodeDecodeError:
                        print("")
                        print("File " + arg + " cannot be found, read or edited")
                        print('Use help --cat to get more information')
                        print("")
                    except FileNotFoundError:
                        print("")
                        print("File " + arg + " not found")
                        print('Use help --cat to get more information')
                        print("")
            elif lex == '':
                pass

            elif lex.lower() == 'rm':
                if arg == '':
                    print("")
                    print("Bad filename")
                    print('Use help --rm to get more information')
                    print("")
                else:
                    try:
                        os.remove(arg)
                    except FileNotFoundError:
                        print("")
                        print("File " + arg + " not found")
                        print('Use help --rm to get more information')
                        print("")



            elif lex.lower() == 'touch':
                if arg == "":
                    print("")
                    print("Bad filename")
                    print('Use help --touch to get more information')
                    print("")
                else: 
                    try:
                        with open(arg, 'w') as lol1:
                            lol1.close()
                    except FileNotFoundError:
                        print("")
                        print("File " + arg + " not found")
                        print("")

                

            elif lex.lower() == 'cp':
                if arg == "":
                    print("")
                    print("Bad filename")
                    print('Use help --cp to get more information')
                    print("")
                else:
                    try:
                        user0 = user.split(' ')
                        shutil.copy2(user0[1], user0[2])
                    except FileNotFoundError:
                        print("I can't found " + user0[1] + " or " + user0[2])
                    except IndexError:
                        print("Not enough arguments!")
                    except PermissionError:
                        try:
                            shutil.copytree(user0[1], user0[2])
                        except:
                            print("I cannot move this object")

            elif lex.lower() == 'wget':
                if arg == "":
                    print("")
                    print("Bad URL")
                    print('Use help --wget to get more information')
                    print("")
                else:
                    print("Trying to download a file...\n")
                    try:
                        wget.download(arg)
                        print("\nFile downloaded!\n")
                    except:
                        print("\nFailed to download file. Maybe it's damaged or you don't have an internet connection\n")
                

            elif lex.lower() == 'ver':
                    print("PyXe ver - " + ver)

            elif lex.lower() == 'exit':
                print("Exit...\nBye! Have a good day! :)\n\n")
                sys.exit()

            else:
                try:
                    eval(arg)
                except SyntaxError:
                    try:
                        runfile(user)
                    except NameError():
                        if arg == "":
                            pass
                        else:
                            print("Name error. Perhaps when trying to open a supposed file called " + arg + ", PyXe was horrified because this file was not found")
                    except:
                        print('An unknown error has occurred :/')
    
        while True:
            cursor = (Fore.LIGHTYELLOW_EX + lib_platform.username + ":(" + os.getcwd() + ")" + Fore.RESET + "\n#: ")
            user = input(cursor)
            if lexer(user): break

    except NameError:
            print("")
            print("It is not a command or an executable")
            print("Try to use help command to get more information")
            print("")

    except AttributeError:
            print("Invalid input >:(")
    
    except KeyboardInterrupt:
        print("")

    except TypeError:
        print("")
        print("Bad argument to command")
        print("Try to use help command to get more information")
        print("")