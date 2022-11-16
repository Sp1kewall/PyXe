#==========================================================================================================================
try:
    import os, sys, time
    from os import *
    def clear():
        c = 'clear'
        if name == 'nt': c = 'cls'
        os.system(c)
    clear()
    import lib_platform
    from colorama import init, Fore
    from colorama import Back
    from pyqadmin import admin 
    from colorama import Style
    from pathlib import Path
    #==========================================================================================================================

    def runfile(x):
        if name == 'nt':
            try:
                os.startfile(x + '.bat')
            except:
                try:
                    os.startfile(x + '.exe')
                except:
                    print(x + " не команда и не исполняемый файл")
        elif name == 'posix':
            try:
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


        elif name == 'posix':
            os.system("nano " + arg)
    #==========================================================================================================================
    os.system("title Space Terminal")
    init(autoreset=True)
    cursor = (Fore.LIGHTGREEN_EX + lib_platform.username + Fore.LIGHTCYAN_EX + "%" + Fore.LIGHTRED_EX + lib_platform.hostname + Fore.LIGHTBLUE_EX + ' ~' + Fore.WHITE + '$:')

    os.chdir(lib_platform.path_userhome)
    clear()
    print("""Space Terminal
    Сделано """ + Fore.YELLOW + """Space Core""" + Fore.WHITE + """
    Мой Discord          --> Space Core#8097
    Мой Steam            --> 1144347594
    Введите команду HELP для вывода списка команд\n\n""")
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
            print("<VER      > просмотреть версию терминала")
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
                    print("Директория " + arg + " не найдена")
                except OSError:
                    print("Произошла непредвиденная ошибка :/")

        elif lex == 'crctl' or lex == 'CRCTL':
            try:
                os.mkdir(arg)
            except OSError:
                print("Дирректория не может быть названа " + arg)
        elif lex == 'rmctl' or lex == 'RMCTL':
                try:
                    os.rmdir(arg)
                except FileNotFoundError:
                    print("Директория " + arg + " не существует")
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
                print("Файл " + arg + " нельзя прочитать")
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
            with open(arg, 'w') as lol:
                lol.close()

        elif lex == 'cname' or lex == 'CNAME':
            if name == 'nt':
                print("Windows")
            elif lex == 'posix':
                print("Linux")

        elif lex == 'ver' or lex == 'VER':
            print("""
        GNU Space Terminal
        Сделано Space Core

        ====================
        Версия терминала 1.4
    """)

        elif lex == 'exit' or lex == 'EXIT':
            print("Выход...\n\n\n")
            sys.exit()

        else:
            runfile(user)
    #==========================================================================================================================
    while True:
        user = input(cursor)
        if lexer(user): break



    #==========================================================================================================================
except KeyboardInterrupt:
            if name == 'nt':
                clear()
                print("Установка модулей...")
                print("\n\n[ lib_platform ]\n\n")
                os.system("pip install lib_platform")
                print("\n\n[ pyqadmin ]\n\n")
                os.system("pip install pyqadmin")
                print("\n\n[ colorama ]\n\n")
                os.system("pip install colorama")
                clear()
                input("Все модули установлены!\n")
            elif name == 'posix':
                clear()
                os.system("sudo apt install python3-pip")
                print("\n\n[ lib_platform ]\n\n")
                os.system("pip install lib_platform")
                print("\n\n[ pyqadmin ]\n\n")
                os.system("pip install pyqadmin")
                print("\n\n[ colorama ]\n\n")
                os.system("pip install colorama")
                clear()
                input("[  OK  ]  Все модули установлены!\n")
except ModuleNotFoundError:
    while True:
        clear()
        ask = input("Модули не установлены или работают не правильно. Нажмите при запуске Ctrl + C для установки всех модулей\nИли установите их сейчас\nУстановить? [y/n] $:")
        if ask == 'y' or ask == 'Y':
            if name == 'nt':
                clear()
                print("Установка модулей...")
                print("\n\n[ lib_platform ]\n\n")
                os.system("pip install lib_platform")
                print("\n\n[ pyqadmin ]\n\n")
                os.system("pip install pyqadmin")
                print("\n\n[ colorama ]\n\n")
                os.system("pip install colorama")
                clear()
                input("Все модули установлены!\n")
            elif name == 'posix':
                clear()
                os.system("sudo apt install python3-pip")
                print("\n\n[ lib_platform ]\n\n")
                os.system("pip install lib_platform")
                print("\n\n[ pyqadmin ]\n\n")
                os.system("pip install pyqadmin")
                print("\n\n[ colorama ]\n\n")
                os.system("pip install colorama")
                clear()
                input("[  OK  ]  Все модули установлены!\n")
        elif ask == 'n' or ask == 'N':
            sys.exit()
        else:
            pass
