ver = "1.8"
discord = "ULTRAKILL </>#8097"


while True:
    try:
        import os, sys, time
        from os import name
        from os import path
        import errors
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
        import shutil
    

        try:
            os.chdir('..')
            lang0 = open('settings/lang.txt', 'r')
            lang = lang0.read()
        except:
            os.startfile('mklang.py')
            input('Press Enter')
            sys.exit()

        if lang == 'rus': #Тут русский | Russian here

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
                            print(x + " не команда и не исполняемый файл")
                            errors.rus.not_command(user)
                elif name == 'posix':
                    try:
                        os.startfile(x)
                    except:
                        print(x + " не команда и не исполняемый файл")
                        errors.rus.not_command(user)
                elif name == 'mac':
                    try:
                        os.startfile(x)
                    except:
                        print(x + " не команда и не исполняемый файл")
                        errors.rus.not_command(user)
            def file(arg):
                if name == 'nt':
                        try:
                            file_path = arg
                            if path.exists(file_path):
                                print("\n\tФайл уже существует!")
                                ans = input("\nВы хотите использовать этот файл? (y/n)\n$:")
                                if ans == 'y' or ans == 'Y':
                                    file = open(file_path, "a")
                                    ans = input("\nВы хотите переписать всё содержимое? (y/n)\n$:")
                                    if ans == 'y' or ans == 'Y':
                                        print("\n\tСтирание...\n")
                                        file.seek(0)
                                        file.truncate()
                                    else:
                                        pass

                                else:
                                    exit()
                            else:
                                print("\n\tСоздание нового файла...\n")
                                file = open(file_path, "a")
                            print("\nНажмите RETURN чтобы начать редактировать следующую строку.\nНажмите Ctrl + C чтобы сохранить и закрыть файл.\n\n")
                            line_count = 1
                            while line_count > 0:
                                try: 
                                    line = input("\t" + str(line_count) + " ")
                                    file.write(line)
                                    file.write('\n')
                                    line_count += 1
                                except KeyboardInterrupt:
                                    print("\n\n\tЗакрытие...")
                                    break

                            file.close()
                        except FileNotFoundError:
                                print("Файл " + arg + " не может быть найден или редактирован")
                                errors.rus.cant_read_error(arg)


                elif name == 'posix' or name == 'mac':
                    os.system("nano " + arg)
        
            os.system("title Space Terminal")


            init(autoreset=True)
            if name == 'mac':
                cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "ˆ" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' ~' + Fore.CYAN + '%:')
            elif name == 'posix':
                cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "ˆ" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' ~' + Fore.CYAN + '$:' + Fore.RESET)
            elif name == 'nt':
                cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "ˆ" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' =' + Fore.WHITE + '>>')


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
            Сделано """ + Fore.YELLOW + """Space Core""" + Fore.WHITE + """
            Мой Discord          --> """ + discord + """
            Мой Steam            --> 1144347594
            Введите команду HELP для вывода списка команд\n\n""")
        
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
                    if arg == '--say':
                        print("SAY - Команда для вывода текста/математического действия на экран\nТекст или математическое действие указывать как аргумент\n\n")
                    elif arg == '--clear':
                        print("CLEAR - Команда для отчистки экрана\n\n")
                    elif arg == '--ls':
                        print("LS - Команда для просмотра содержимого директории. Если объект выделен зеленым, значит это директория\n\n")
                    elif arg == '--wia':
                        print("WIA - Команда для вывода текущего пути\n\n")
                    elif arg == '--cd':
                        print("CD - Команда для смены директории\nИмя директории указывать как аргумент\n\n")
                    elif arg == '--crctl':
                        print("CRCTL - Команда для создания директории\nИмя директории указывать как аргумент\n\n")
                    elif arg == '--rmctl':
                        print("CRCTL - Команда для удаления директории\nИмя директории указывать как аргумент\n\n")
                    elif arg == '--rm':
                        print("RM - Команда для удаления файла\nИмя файла указывать как аргумент")
                    elif arg == '--file':
                        print("FILE - Команда для открытия текстового редактора (в macOS и Linux это nano, в Windows это встроеный редактор\nИмя файла указывать как аргумент\n\n")
                    elif arg == '--touch':
                        print("TOUCH - Команда для создания файла без редактирования\nИмя файла указывать как аргумент\n\n")
                    elif arg == '--cat':
                        print("CAT - Команда для вывода содержимого файла\nИмя файла указывать как аргумент\n\n")
                    elif arg == "--ver":
                        print("VER - Ккоманда для вывода информации о версии\n\n")
                    elif arg == '--upt':
                        print("[BETA] UPT - Команда для загрузки новой версии Space Terminal на ваш ПК\nВАЖНО !ОБНОВЛЕНИЕ НЕ ВЫПОЛНЯЕТСЯ АВТОМАТИЧЕСКИ!\n\n")
                    else:
                        print("<HELP     > вывести список команд")
                        print("<SAY      > вывести какой-то текст")
                        print("<CLEAR    > отчистить экран")
                        print("<LS       > просмотреть содержимое текущей директории")
                        print("<WIA      > просмотреть путь к текущей директории")
                        print("<CD       > сменить директорию")
                        print("<CRCTL    > создать директорию")
                        print("<RMCTL    > удалить директорию")
                        print("<RM       > удалить выбранный файл")
                        print("<FILE     > открыть текстовый редактор")
                        print("<TOUCH    > создать файл без редактирования")
                        print("<CAT      > вывести содержимое файла")
                        print("<UPT      > Загрузить новую версию Space Terminal ")
                        print("<VER      > просмотреть версию терминала")
                elif lex == 'say' or lex == 'SAY':
                    try:
                        print(eval(arg))
                    except SyntaxError:
                        print(arg)
                    except ZeroDivisionError:
                        print("На ноль делить нельзя")
                        errors.rus.zero_dev()
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
                            print("Директория " + arg + " не найдена")
                            errors.rus.dir_is_not_exist(arg)
                        except:
                            print("Произошла непредвиденная ошибка :/")
                            errors.rus.idk()

                elif lex == 'crctl' or lex == 'CRCTL':
                    try:
                        os.mkdir(arg)
                    except OSError:
                        print("Директория не может быть названа " + arg)
                        errors.rus.dir_name_error(arg)
                elif lex == 'rmctl' or lex == 'RMCTL':
                        try:
                            os.rmdir(arg)
                        except FileNotFoundError:
                            print("Директория " + arg + " не найдена")
                            errors.rus.dir_is_not_exist(arg)
                        except OSError:
                            try:
                                shutil.rmtree('Space-Terminal-main')
                            except:
                                print("Директория не может быть названа " + arg)
                                errors.rus.dir_name_error(arg)
                elif lex == 'file' or lex == 'FILE':
                    file(arg)
                elif lex == 'cat' or lex == 'CAT':
                    try:
                        f = open(arg, 'r')
                        print(f.read())
                        f.close()
                    except UnicodeDecodeError:
                        print("Файл " + arg + " не может быть найден, прочитан или отредактирован")
                        errors.rus.cant_read_error(arg)
                    except FileNotFoundError:
                        print("Файл " + arg + " не найден")
                        errors.rus.no_file_error(arg)
                elif lex == '':
                    pass
                elif lex == 'rm' or lex == 'RM':
                        try:
                            os.remove(arg)
                        except FileNotFoundError:
                            print("Файл " + arg + " не найден")
                            errors.rus.no_file_error(arg)

                elif lex == 'user' or lex == 'USER':
                    print(Fore.GREEN + lib_platform.username)

                elif lex == 'host' or lex == 'HOST':
                    print(Fore.RED + lib_platform.hostname)

                elif lex == 'touch' or lex == 'TOUCH':
                    try:
                        with open(arg, 'w') as lol:
                            lol.close()
                    except FileNotFoundError:
                        print("Файл " + arg + " не найден")
                        errors.rus.no_file_error(arg)

                elif lex == 'cname' or lex == 'CNAME':
                    if name == 'nt':
                        print("Windows")
                    elif lex == 'posix':
                        print("UNIX Linux")
                    elif lex == 'mac':
                        print("UNIX OS X")

                elif lex == 'UPT' or lex == 'upt':
                    # print("This function is not work now, but i will fix this one\nMaybe...")    ТЕПЕРЬ ОНО РАБОТАЕТ!
                    os.chdir(cdir)
                    os.chdir("..")
                    download_file('https://github.com/SpaceCoreOfficial/Space-Terminal/archive/refs/heads/main.zip')
                    os.chdir("utilities")
                    os.startfile("download.py")
                    sys.exit()
                    

                elif lex == 'ver' or lex == 'VER':
                    print("""
                    |OpenSource|
                  |Space Terminal|
                |Сделано Space Core|

                ____________________
                    Версия """ + ver + "\n")

                elif lex == 'exit' or lex == 'EXIT':
                    print("Выход...\nПока! Хорошего дня! :)\n\n")
                    sys.exit()

                else:
                    try:
                        print(eval(arg))
                    except SyntaxError:
                        try:
                            runfile(user)
                        except:
                            errors.rus.idk()
        
            while True:
                user = input(cursor)
                if lexer(user): break



        
        elif lang == 'eng': #English here | Тут английский















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
                            errors.eng.not_command(user)
                elif name == 'posix':
                    try:
                        os.startfile(x)
                    except:
                        print(x + " is not a command or an executable")
                        errors.eng.not_command(user)
                elif name == 'mac':
                    try:
                        os.startfile(x)
                    except:
                        print(x + " is not a command or an executable")
                        errors.eng.not_command(user)
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
                                        print("\n\tСтирание...\n")
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
                                errors.eng.cant_read_error(arg)


                elif name == 'posix' or name == 'mac':
                    os.system("nano " + arg)
        
            os.system("title Space Terminal")


            init(autoreset=True)
            if name == 'mac':
                cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "ˆ" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' ~' + Fore.CYAN + '%:')
            elif name == 'posix':
                cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "ˆ" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' ~' + Fore.CYAN + '$:' + Fore.RESET)
            elif name == 'nt':
                cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "ˆ" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' =' + Fore.WHITE + '>>')


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
            My Discord          --> """ + discord + """
            My Steam            --> 1144347594
            Enter the HELP command to display a list of commands\n\n""")
        
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
                        errors.eng.zero_dev()
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
                            errors.eng.dir_is_not_exist(arg)
                        except:
                            print("An unexpected error has occurred :/")
                            errors.eng.idk()

                elif lex == 'crctl' or lex == 'CRCTL':
                    try:
                        os.mkdir(arg)
                    except OSError:
                        print("Directory cannot be named " + arg)
                        errors.eng.dir_name_error(arg)
                elif lex == 'rmctl' or lex == 'RMCTL':
                        try:
                            os.rmdir(arg)
                        except FileNotFoundError:
                            print("Directory " + arg + " not exist")
                            errors.eng.dir_is_not_exist(arg)
                        except OSError:
                            try:
                                shutil.rmtree('Space-Terminal-main')
                            except:
                                print("Directory cannot be named " + arg)
                                errors.eng.dir_name_error(arg)
                elif lex == 'file' or lex == 'FILE':
                    file(arg)
                elif lex == 'cat' or lex == 'CAT':
                    try:
                        f = open(arg, 'r')
                        print(f.read())
                        f.close()
                    except UnicodeDecodeError:
                        print("File " + arg + " cannot be found, read or edited")
                        errors.eng.cant_read_error(arg)
                    except FileNotFoundError:
                        print("File " + arg + " not found")
                        errors.eng.no_file_error(arg)
                elif lex == '':
                    pass
                elif lex == 'rm' or lex == 'RM':
                        try:
                            os.remove(arg)
                        except FileNotFoundError:
                            print("File " + arg + " not found")
                            errors.eng.no_file_error(arg)

                elif lex == 'user' or lex == 'USER':
                    print(Fore.GREEN + lib_platform.username)

                elif lex == 'host' or lex == 'HOST':
                    print(Fore.RED + lib_platform.hostname)

                elif lex == 'touch' or lex == 'TOUCH':
                    try:
                        with open(arg, 'w') as lol:
                            lol.close()
                    except FileNotFoundError:
                        print("File " + arg + " not found")
                        errors.eng.no_file_error(arg)

                elif lex == 'cname' or lex == 'CNAME':
                    if name == 'nt':
                        print("Windows")
                    elif lex == 'posix':
                        print("UNIX Linux")
                    elif lex == 'mac':
                        print("UNIX OS X")

                elif lex == 'UPT' or lex == 'upt':
                    # print("This function is not work now, but i will fix this one\nMaybe...")    NOW IT'S WORKING!
                    os.chdir(cdir)
                    os.chdir("..")
                    download_file('https://github.com/SpaceCoreOfficial/Space-Terminal/archive/refs/heads/main.zip')
                    os.chdir("utilities")
                    os.startfile("download.py")
                    sys.exit()
                    

                elif lex == 'ver' or lex == 'VER':
                    print("""
                |OpenSource|
              |Space Terminal|
            |Made by Space Core|
            
            ____________________
                 Version """ + ver + "\n")

                elif lex == 'exit' or lex == 'EXIT':
                    print("Exit...\nBye! Have a good day! :)\n\n")
                    sys.exit()

                else:
                    try:
                        print(eval(arg))
                    except SyntaxError:
                        try:
                            runfile(user)
                        except:
                            errors.eng.idk()
        
            while True:
                user = input(cursor)
                if lexer(user): break



    except KeyboardInterrupt:
                    clear()
                    if lang == 'rus':
                        print("Установка модулей...")
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
                            input("[  OK  ]  Все модули установлены!\n")
                        elif name == 'posix':
                            clear()
                            var1 = input("Установить pip?\n(y/n)$:")
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
                            input("[  OK  ]  Все модули установлены!\n")
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
                            input("[  OK  ]  Все модули установлены!\n")

                    elif lang == 'eng':

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
                if lang == 'rus':
                    ask = input("Модули не установлены или работают не правильно. Нажмите при запуске Ctrl + C для установки всех модулей\nИли установите их сейчас\nУстановить? [y/n] $:")
                    if ask == 'y' or ask == 'Y':
                        print("Установка модулей...")
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
                            input("[  OK  ]  Все модули установлены!\n")
                        elif name == 'posix':
                            clear()
                            var1 = input("Установить pip?\n(y/n)$:")
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
                            input("[  OK  ]  Все модули установлены!\n")
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
                            input("[  OK  ]  Все модули установлены!\n")
                    elif ask == 'n' or ask == 'N':
                        sys.exit()
                    else:
                        pass

                elif lang == 'eng':
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

    except NameError:
        if lang == 'rus':
            errors.rus.idk()
        elif lang == 'eng':
            errors.eng.idk()
        
        sys.exit()
