ver = "1.7"
discord = "ULTRAKILL </>#8097"

#==========================================================================================================================
while True:
    try:
        import os, sys, time
        from os import name
        from os import path
        def clear():
            c = 'clear'
            if name == 'nt': c = 'cls'
            os.system(c)
        clear()
        import lib_platform
        import requests
        from colorama import init, Fore
        from colorama import Back
        from pyqadmin import admin 
        from colorama import Style
        from pathlib import Path
        import zipfile
    #==========================================================================================================================

        def download_file(url):
            local_filename = url.split('/')[-1]
            with requests.get(url, stream=True, allow_redirects=True) as r:
                r.raise_for_status()
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192): 
                        f.write(chunk)
            return local_filename

        def runfile(x):
            if name == 'nt':
                try:
                    os.startfile(x + '.bat')
                except:
                    try:
                        os.startfile(x + '.exe')
                    except:
                        print(x + " is not a command or an executable")
            elif name == 'posix':
                try:
                    os.startfile(x)
                except:
                    print(x + " is not a command or an executable")
            elif name == 'mac':
                try:
                    os.startfile(x)
                except:
                    print(x + " is not a command or an executable")
        def file(arg):
            if name == 'nt':
                    try:
                        file_path = arg
                        if path.exists(file_path):
                            print("\n\tThe file already exists!")
                            ans = input("\nDo you want to use this file? (y/n)\n$:")
                            if ans == 'y' or ans == 'Y':
                                file = open(file_path, "a")
                                ans = input("\nDo you want to overwrite all content? (y/n)\n$:")
                                if ans == 'y' or ans == 'Y':
                                    print("\n\tErasing...\n")
                                    file.seek(0)
                                    file.truncate()
                                else:
                                    pass

                            else:
                                exit()
                        else:
                            print("\n\tCreating a new file....\n")
                            file = open(file_path, "a")
                        print("\nPress RETURN to start editing the next line.\nPress Ctrl + C to save and close the file.\n\n")
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
                            print("File " + arg + " cannot be found or edited")


            elif name == 'posix' or name == 'mac':
                os.system("nano " + arg)
    #==========================================================================================================================
        os.system("title Space Terminal")
        init(autoreset=True)
        if name == 'mac':
            cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "ˆ" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' ~' + Fore.CYAN + '%:')
        elif name == 'posix':
            cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "ˆ" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' ~' + Fore.CYAN + '$:' + Fore.RESET)
        elif name == 'nt':
            cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "ˆ" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' =' + Fore.WHITE + '>>')

        os.chdir("..")

        if os.path.isfile("settings/cdir.txt"):
                cdir0 = open("settings/cdir.txt", "r")
                cdir = cdir0.read()
        else:
            lol = open("settings/cdir.txt", 'w')
            lol.writelines(os.getcwd())
            lol.close()
            cdir0 = open("settings/cdir.txt", "r")
            cdir = cdir0.read()

        os.chdir(lib_platform.path_userhome)
        clear()
        print("""Space Terminal
        Made by """ + Fore.YELLOW + """Space Core""" + Fore.WHITE + """
        My Discord          --> Space Core#8097
        My Steam            --> 1144347594
        Enter the HELP command to display a list of commands\n\n""")
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
                if arg == '--say':
                    print("SAY - Command for displaying text/math on the screen\nSpecify text or mathematical action as an argument\n\n")
                elif arg == '--clear':
                    print("CLEAR - Command to clear the screen\n\n")
                elif arg == '--ls':
                    print("LS - Command to view the contents of a directory. If the object is highlighted in green, then this is a directory\n\n")
                elif arg == '--wia':
                    print("WIA - Command to display the current path\n\n")
                elif arg == '--cd':
                    print("CD - Command to change directory\nDirectory name as an argument\n\n")
                elif arg == '--crctl':
                    print("CRCTL - Command to create a directory\nDirectory name as an argument\n\n")
                elif arg == '--rmctl':
                    print("CRCTL - Command to remove a directory\nDirectory name as an argument\n\n")
                elif arg == '--rm':
                    print("RM - Command to delete a file\nThe file name is given as an argument")
                elif arg == '--file':
                    print("FILE - Command to open a text editor (on macOS and Linux it's nano, on Windows it's a built-in editor)\nThe file name is given as an argument\n\n")
                elif arg == '--touch':
                    print("TOUCH - Command to create a file without editing\nThe file name is given as an argument\n\n")
                elif arg == '--cat':
                    print("CAT - Command to display the contents of a file\nThe file name is given as an argument\n\n")
                elif arg == '--upt':
                    print("[BETA] UPT - The command to download the new version of Space Terminal to your PC\nIMPORTANT! UPDATE IS NOT PERFORMED AUTOMATICALLY!\n\n")
                elif arg == "--ver":
                    print("VER - Command to display version information\n\n")
                else:
                    print("<HELP     > list commands")
                    print("<SAY      > output some text")
                    print("<CLEAR    > clear screen")
                    print("<LS       > view the contents of the current directory")
                    print("<WIA      > view the path to the current directory")
                    print("<CD       > change directory")
                    print("<CRCTL    > create a directory")
                    print("<RMCTL    > delete directory")
                    print("<RM       > delete selected file")
                    print("<FILE     > open text editor")
                    print("<TOUCH    > create file without editing")
                    print("<CAT      > output the contents of the file")
                    print("<UPT      > Download the new version of Space Terminal")
                    print("<VER      > view terminal version")
            elif lex == 'say' or lex == 'SAY':
                try:
                    print(eval(arg))
                except SyntaxError:
                    print(arg)
                except ZeroDivisionError:
                    print("Can't divide by zero")
                except NameError:
                    print(arg)

            elif lex == 'ls' or lex == 'LS':
                rez = sorted(os.listdir("."))
                for n, item in enumerate(rez):
                    if os.path.isdir(item):
                        print(Back.GREEN + item)
                    elif os.path.isfile(item):
                        print(item)

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
                        print("Directory " + arg + " not exist")
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
                    print("File " + arg + " unreadable")
                except FileNotFoundError:
                    print("File or dir with this name not found")
            elif lex == '':
                pass
            elif lex == 'rm' or lex == 'RM':
                    try:
                        os.remove(arg)
                    except FileNotFoundError:
                        print("File " + arg + " not found")

            elif lex == 'user' or lex == 'USER':
                print(Fore.GREEN + lib_platform.username)

            elif lex == 'host' or lex == 'HOST':
                print(Fore.RED + lib_platform.hostname)

            elif lex == 'touch' or lex == 'TOUCH':
                try:
                    with open(arg, 'w') as lol:
                        lol.close()
                except FileNotFoundError:
                    print("File or dir with this name not found")

            elif lex == 'cname' or lex == 'CNAME':
                if name == 'nt':
                    print("Windows")
                elif lex == 'posix':
                    print("UNIX Linux")
                elif lex == 'mac':
                    print("UNIX OS X")

            elif lex == 'UPT' or lex == 'upt':
                print("This function is not work now, but i will fix this one\nMaybe...")
                # os.chdir(cdir)
                # os.chdir("..")
                # download_file('https://github.com/SpaceCoreOfficial/Space-Terminal/archive/refs/heads/main.zip')
                # os.chdir("utilities")
                # os.startfile("download.py")
                # sys.exit()

            elif lex == 'ver' or lex == 'VER':
                print("""
            Space Terminal (OpenSource)
            Made by Space Core
            ====================
                 Version """ + ver + "\n")

            elif lex == 'exit' or lex == 'EXIT':
                print("Exit...\nBye! Have a good day! :)\n\n")
                sys.exit()

            else:
                try:
                    print(eval(arg))
                except SyntaxError:
                    runfile(user)
    #==========================================================================================================================
        while True:
            user = input(cursor)
            if lexer(user): break



    #==========================================================================================================================
    except KeyboardInterrupt:
                clear()
                print("Installing modules...")
                if name == 'nt':
                    clear()
                    print("\n\n[ lib_platform ]\n\n")
                    os.system("pip install lib_platform")
                    print("\n\n[ pyqadmin ]\n\n")
                    os.system("pip install pyqadmin")
                    print("\n\n[ colorama ]\n\n")
                    os.system("pip install colorama")
                    print("\n\nRequests\n\n")
                    os.system("pip install requests")
                    print("\n\nZipFile\n\n")
                    clear()
                    input("[  OK  ]  All modules installed!\n")
                elif name == 'posix':
                    clear()
                    var1 = input("Install pip?\n(y/n)$:")
                    if var1 == 'y' or var1 == "Y":
                        os.system("sudo apt install python3-pip")
                    else:
                        pass
                    print("\n\n[ lib_platform ]\n\n")
                    os.system("pip install lib_platform")
                    print("\n\n[ pyqadmin ]\n\n")
                    os.system("pip install pyqadmin")
                    print("\n\n[ colorama ]\n\n")
                    os.system("pip install colorama")
                    print("\n\nRequests\n\n")
                    os.system("pip install requests")
                    print("\n\nZipFile\n\n")
                    clear()
                    input("[  OK  ]  All modules installed!\n")
                elif name == 'mac':
                    print("\n\n[ lib_platform ]\n\n")
                    os.system("pip3 install lib_platform")
                    print("\n\n[ pyqadmin ]\n\n")
                    os.system("pip3 install pyqadmin")
                    print("\n\n[ colorama ]\n\n")
                    os.system("pip install colorama")
                    print("\n\nRequests\n\n")
                    os.system("pip install requests")
                    print("\n\nZipFile\n\n")
                    clear()
                    input("[  OK  ]  All modules installed!\n")
    except ModuleNotFoundError:
        while True:
            clear()
            ask = input("Modules are not installed or are not working correctly. Press Ctrl + C at startup to install all modules\nOr install them now\nInstall? [y/n] $:")
            if ask == 'y' or ask == 'Y':
                print("Installing modules...")
                if name == 'nt':
                    clear()
                    print("\n\n[ lib_platform ]\n\n")
                    os.system("pip install lib_platform")
                    print("\n\n[ pyqadmin ]\n\n")
                    os.system("pip install pyqadmin")
                    print("\n\n[ colorama ]\n\n")
                    os.system("pip install colorama")
                    print("\n\nRequests\n\n")
                    os.system("pip install requests")
                    print("\n\nZipFile\n\n")
                    clear()
                    input("[  OK  ]  All modules installed!\n")
                elif name == 'posix':
                    clear()
                    var1 = input("Install pip?\n(y/n)$:")
                    if var1 == 'y' or var1 == "Y":
                        os.system("sudo apt install python3-pip")
                    else:
                        pass
                    print("\n\n[ lib_platform ]\n\n")
                    os.system("pip install lib_platform")
                    print("\n\n[ pyqadmin ]\n\n")
                    os.system("pip install pyqadmin")
                    print("\n\n[ colorama ]\n\n")
                    os.system("pip install colorama")
                    print("\n\nRequests\n\n")
                    os.system("pip install requests")
                    print("\n\nZipFile\n\n")
                    clear()
                    input("[  OK  ]  All modules installed!\n")
                elif name == 'mac':
                    print("\n\n[ lib_platform ]\n\n")
                    os.system("pip3 install lib_platform")
                    print("\n\n[ pyqadmin ]\n\n")
                    os.system("pip3 install pyqadmin")
                    print("\n\n[ colorama ]\n\n")
                    os.system("pip3 install colorama")
                    print("\n\nRequests\n\n")
                    os.system("pip install requests")
                    print("\n\nZipFile\n\n")
                    clear()
                    input("[  OK  ]  All modules installed!\n")
            elif ask == 'n' or ask == 'N':
                sys.exit()
            else:
                pass
