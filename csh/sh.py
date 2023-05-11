ver = "2.0"

while True:
    try:
        import os, sys
        from os import name
        from os import path
        from tkinter import messagebox
        def clear():
            c = 'clear'
            if name == 'nt': c = 'cls'
            os.system(c)
        clear()



        try:
            lang0 = open('lang.txt', 'r')
            lang = lang0.read()
        except:
            while True:
                if os.path.isfile('lang.txt'):
                    break
                else:
                    clear()
                    lang_ask = input("""
                Choose your language:
                Выберите свой язык:

                \t 1.Русский (Russian)
                \t 2.English (Английский)
                $:""")
                    lang01 = open('lang.txt', 'w')
                    if lang_ask == '1':
                        lang01.write('rus')
                    elif lang_ask == '2':
                        lang01.write('eng')
                    else:
                        pass
                    lang01.close()
                    lang01 = open('lang.txt', 'r')
                    lang = lang01.read()

        if os.path.isfile("cdir.txt"):
                cdir0 = open("cdir.txt", "r")
                cdir = cdir0.read()
        else:
            lol = open("cdir.txt", 'w')
            lol.writelines(os.getcwd())
            lol.close()
            cdir0 = open("cdir.txt", "r")
            cdir = cdir0.read()


        import lib_platform
        import requests
        from colorama import init, Fore
        from colorama import Back
        from pyqadmin import admin 
        from colorama import Style
        from pathlib import Path
        import shutil

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
                    try:
                        if name == 'nt':
                            os.system(x)
                        else:
                            os.startfile(x)
                    except:
                            print(x + " не команда и не исполняемый файл")

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



                elif name == 'posix' or name == 'mac':
                    os.system("nano " + arg)
        


            def hstry():
                with open(cdir + '/history', 'a') as hst:
                    hst.writelines('\n' + user)
                hst.close()


            cursor = (Fore.LIGHTCYAN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + Fore.RESET + "ˆ" + Fore.LIGHTMAGENTA_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + " ~~ " + Fore.CYAN + '>_<  ' + Fore.RESET) 


            init(autoreset=True)



            os.chdir(lib_platform.path_userhome)
            clear()
            print("CShell была запущена\nCShell - Сделано " + Fore.LIGHTYELLOW_EX + "Space Core" + Fore.RESET + '\n')
            print("User - " + lib_platform.username)
            print("Введите команду HELP чтобы получить справку")
            print("Host - " + lib_platform.hostname + "\n\n")
        
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
                        print("LS - Команда для просмотра содержимого директории. Если объект выделен зеленым, значит это директория.\nЕсли объект имеет красный фон, то это защищённая директория, а если красный текст, то это защищённый файл\nЗащищённые файлы и директории нельзя удалить!\n\n")
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
                    elif arg == '--cp':
                        print("CP - Команда для копирования файла из одной директории в другую (если во втором аргументе указан файл, то в него скопируется содержимое первого аргумена)\nВ первом аргументе указывать копируемый файл. Во втором аргументе указывать конечный путь\n\n")
                    elif arg == '--wget':
                        print("WGET - Команда для скачивания файла из интернета\nВ аргументе указывать ссылку на скачивание\n\n")
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
                        print("<CP       > скопировать файл в какое-то место или файл")
                        print('<WGET     > скачать файл из интернета')
                        print("<VER      > просмотреть версию терминала")
                elif lex == 'say' or lex == 'SAY':
                    try:
                        print(eval(arg))
                    except SyntaxError:
                        print(arg)
                    except ZeroDivisionError:
                        print("На ноль делить нельзя")

                    except NameError:
                        print(arg)

                elif lex == 'ls' or lex == 'LS':
                    try:
                        rez = sorted(os.listdir("."))
                        for n, item in enumerate(rez):
                            if os.path.isdir(item):
                                    print(Back.GREEN + item)
                            elif os.path.isfile(item):
                                    print(item)
                    except PermissionError:
                        print('Мне отказано в доступе')

                elif lex == 'wia' or lex == 'WIA':
                    print(os.getcwd())
                elif lex == 'clear' or lex == 'CLEAR':
                    clear()

                elif lex == 'cd' or lex == 'CD':
                        try:
                            os.chdir(arg)
                        except FileNotFoundError:
                            print("Директория " + arg + " не найдена")

                        except OSError:
                            print("Недостаточно аргументов")
                        except:
                            print("Произошла непредвиденная ошибка :/")


                elif lex == 'crctl' or lex == 'CRCTL':
                    try:
                        os.mkdir(arg)
                    except OSError:
                        print("Директория не может быть названа " + arg)

                elif lex == 'rmctl' or lex == 'RMCTL':
                        try:
                                shutil.rmtree(arg)
                        except FileNotFoundError:
                            print("Директория " + arg + " не найдена")

                        except OSError:
                                print("Директория не может быть названа " + arg)

                elif lex == 'file' or lex == 'FILE':
                    file(arg)
                elif lex == 'cat' or lex == 'CAT':
                    try:
                        f = open(arg, 'r')
                        print(f.read())
                        f.close()
                    except UnicodeDecodeError:
                        print("Файл " + arg + " не может быть найден, прочитан или отредактирован")

                    except FileNotFoundError:
                        print("Файл " + arg + " не найден")

                elif lex == '':
                    pass
                elif lex == 'rm' or lex == 'RM':
                        try:
                                os.remove(arg)
                        except FileNotFoundError:
                            print("Файл " + arg + " не найден")


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


                elif lex == 'cname' or lex == 'CNAME':
                    if name == 'nt':
                        print("Windows")
                    elif lex == 'posix':
                        print("UNIX Linux")
                    elif lex == 'mac':
                        print("UNIX OS X")



                elif lex == 'cp':
                    try:
                        user0 = user.split(' ')
                        shutil.copy2(user0[1], user0[2])
                    except FileNotFoundError:
                        print("Я не нашёл элементов " + user0[1] + " или " + user0[2])
                    except IndexError:
                        print("Недостаточно аргументов!")
                    except PermissionError:
                        try:
                            shutil.copytree(user0[1], user0[2])
                        except:
                            print("Я не могу переместить этот объект")


                elif lex == 'wget' or lex == 'WGET':
                    print("Пытаюсь скачать файл...\n")
                    try:
                        download_file(arg)
                        print("Файл скачан!\n")
                    except:
                        print("Не удалось скачать файл. Возможно он повреждён или у вас нет подключение к интернету\n")
                    

                elif lex == 'ver' or lex == 'VER':
                    print("""
                |OpenSource               |
                |CSh (Space Terminal)     |
                |Сделано Space Core       |

                __________________________
                         Версия """ + ver + "\n\n")

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
                            print("Произошла неизвестная ошибка :/")
        
            while True:
                user = input(cursor)
                if lexer(user): break

                elif os.path.isfile(cdir + '/history'):
                    hstry()
                else:
                    hh = open(cdir + '/history', 'w')

                    hh.close()
                    hstry()


        
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
                    try:
                        if name == 'nt':
                            os.system(x)
                        else:
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


                elif name == 'posix' or name == 'mac':
                    os.system("nano " + arg)
        


            def hstry():
                with open(cdir + '/history', 'a') as hst:
                    hst.writelines('\n' + user)
                hst.close()


            init(autoreset=True)
            cursor = (Fore.LIGHTCYAN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + Fore.RESET + "ˆ" + Fore.LIGHTMAGENTA_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + " ~~ " + Fore.CYAN + '>_<  ' + Fore.RESET) 


            if os.path.isfile("!settings/cdir.txt"):
                    cdir0 = open("!settings/cdir.txt", "r")
                    cdir = cdir0.read()
            else:
                lol = open("!settings/cdir.txt", 'w')
                lol.writelines(os.getcwd())
                lol.close()
                cdir0 = open("!settings/cdir.txt", "r")
                cdir = cdir0.read()

            os.chdir(lib_platform.path_userhome)
            clear()
            print("CShell was started\nCShell - Made by " + Fore.LIGHTYELLOW_EX + "Space Core" + Fore.RESET + '\n')
            print("Enter HELP commant for help")
            print("User - " + lib_platform.username)
            print("Host - " + lib_platform.hostname + "\n\n")
        
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
                    elif arg == "--ver":
                        print("VER - Command to display version information\n\n")
                    elif arg == '--cp':
                        print("CP - Command for copying a file from one directory to another (if a file is specified in the second argument, then the contents of the first argument will be copied to it)\nSpecify the file to be copied as the first argument. Specify the final path in the second argument\n\n")
                    elif arg == '--wget':
                        print("WGET - Command to download a file from the Internet\nSpecify the download link in the argument\n\n")
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
                        print("<CP       > copy the file to some location or file")
                        print('<WGET     > download file from internet')
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
                    try:
                        rez = sorted(os.listdir("."))
                        for n, item in enumerate(rez):
                            if os.path.isdir(item):
                                print(Back.GREEN + item)
                            elif os.path.isfile(item):
                                print(item)
                    except PermissionError:
                        print('I was denied access')

                elif lex == 'wia' or lex == 'WIA':
                    print(os.getcwd())
                elif lex == 'clear' or lex == 'CLEAR':
                    clear()

                elif lex == 'cd' or lex == 'CD':
                        try:
                            os.chdir(arg)
                        except FileNotFoundError:
                            print("Directory " + arg + " not found")
                        except:
                            print("An unexpected error has occurred :/")

                elif lex == 'crctl' or lex == 'CRCTL':
                    try:
                        os.mkdir(arg)
                    except OSError:
                        print("Directory cannot be named " + arg)
                elif lex == 'rmctl' or lex == 'RMCTL':
                        try:
                                shutil.rmtree(arg)
                        except FileNotFoundError:
                            print("Directory " + arg + " not found")

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
                        print("File " + arg + " cannot be found, read or edited")
                    except FileNotFoundError:
                        print("File " + arg + " not found")
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
                        print("File " + arg + " not found")

                    

                elif lex == 'cp':
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

                elif lex == 'wget' or lex == 'WGET':
                    print("Trying to download a file...\n")
                    try:
                        download_file(arg)
                        print("File downloaded!\n")
                    except:
                        print("Failed to download file. Maybe it's damaged or you don't have an internet connection\n")
                    

                elif lex == 'ver' or lex == 'VER':
                    print("""
                |OpenSource               |
                |CSh (Space Terminal)     |
                |Made by Space Core       |
            
                __________________________
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
                            messagebox.showerror('Error', 'An unknown error has occurred :/')
        
            while True:
                user = input(cursor)
                if lexer(user): break

                elif os.path.isfile(cdir + '/history'):
                    hstry()
                else:
                    hh = open(cdir + '/history', 'w')

                    hh.close()
                    hstry()



    except KeyboardInterrupt:
                    os.chdir(cdir)
                    clear()
                    if lang == 'rus':
                        print("Установка модулей...")
                        if name == 'nt':
                            clear()
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  Все модули обновлены! Нажмите ENTER чтобы перезапустить оболочку\n")
                        elif name == 'posix':
                            clear()
                            var1 = input("Установить pip?\n(y/n)$:")
                            if var1 == 'y' or var1 == "Y":
                                os.system("sudo apt install python3-pip")
                            else:
                                pass
                            clear()
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  Все модули обновлены! Нажмите ENTER чтобы перезапустить оболочку\n")
                        elif name == 'mac':
                            clear()
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  Все модули обновлены! Нажмите ENTER чтобы перезапустить оболочку\n")

                    elif lang == 'eng':

                        print("Installing modules...")
                        if name == 'nt':
                            clear()
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  All modules have been updated! Press ENTER to restart the shell\n")
                            sys.exit()
                        elif name == 'posix':
                            clear()
                            var1 = input("Install pip?\n(y/n)$:")
                            if var1 == 'y' or var1 == "Y":
                                os.system("sudo apt install python3-pip")
                            else:
                                pass
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  All modules have been updated! Press ENTER to restart the shell\n")
                            sys.exit()
                        elif name == 'mac':
                            clear()
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  All modules have been updated! Press ENTER to restart the shell\n")
                            sys.exit()

    except ModuleNotFoundError:
            while True:
                clear()
                if lang == 'rus':
                    print(os.getcwd())
                    ask = input("Модули не установлены или работают не правильно. Нажмите при запуске Ctrl + C для установки всех модулей\nИли установите их сейчас\nУстановить? [y/n] $:")
                    if ask == 'y' or ask == 'Y':
                        print("Установка модулей...")
                        if name == 'nt':
                            clear()
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  Все модули установлены! Нажмите ENTER чтобы перезапустить оболочку\n")
                            sys.exit()
                        elif name == 'posix':
                            clear()
                            var1 = input("Установить pip?\n(y/n)$:")
                            if var1 == 'y' or var1 == "Y":
                                os.system("sudo apt install python3-pip")
                            else:
                                pass
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  Все модули установлены! Нажмите ENTER чтобы перезапустить оболочку\n")
                            sys.exit()
                        elif name == 'mac':
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  Все модули установлены! Нажмите ENTER чтобы перезапустить оболочку\n")
                            sys.exit()
                    elif ask == 'n' or ask == 'N':
                        sys.exit()
                    else:
                        print("Ты серьёзно?")

                elif lang == 'eng':
                    ask = input("Modules are not installed or are not working correctly. Press Ctrl + C at startup to install all modules\nOr install them now\nInstall? [y/n] $:")
                    if ask == 'y' or ask == 'Y':
                        print("Installing modules...")
                        if name == 'nt':
                            clear()
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  All modules are installed! Press ENTER to restart the shell\n")
                        elif name == 'posix':
                            clear()
                            var1 = input("Install pip?\n(y/n)$:")
                            if var1 == 'y' or var1 == "Y":
                                os.system("sudo apt install python3-pip")
                            else:
                                pass
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  All modules are installed! Press ENTER to restart the shell\n")
                        elif name == 'mac':
                            os.system("pip install -r requirements.txt")
                            clear()
                            input("[  OK  ]  All modules are installed! Press ENTER to restart the shell\n")

                    elif ask == 'n' or ask == 'N':
                        sys.exit()


                    else:
                        print("Are you serious?")

    except NameError:
        if lang == 'rus':
            messagebox.showerror('Ошибка', 'Произошла неизвестная ошибка :/')
        elif lang == 'eng':
            messagebox.showerror('Error', 'An unknown error has occurred :/')
      
        sys.exit()
        
