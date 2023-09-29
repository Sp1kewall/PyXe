ver = "2.6"
special = ["└", "┘", "┌", "┐", "├", "┤", "─", "│"]
while True:
    try:
        import os, sys
        from os import name
        import lib_platform
        from colorama import init, Fore
        from colorama import Back
        import wget
        import shutil
        from prompt_toolkit import prompt
        from prompt_toolkit.formatted_text import HTML

        def clear():
            if name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        try:
            lang0 = open(lib_platform.path_userhome + "/PyXes/pies/lang.pie", 'r')
            lang = lang0.read()
        except:
            while True:
                if os.path.isfile(lib_platform.path_userhome + "/PyXes/pies/lang.pie") and os.path.isdir(lib_platform.path_userhome + "/PyXes/pies"):
                    break
                else:
                    lang_status = "1"
                    lang_ask = input("""
                Choose your language:
                Выберите свой язык:

                \t 1.Русский (Russian)
                \t 2.English (Английский)
                $:""")
                    os.mkdir(lib_platform.path_userhome + "/PyXes")
                    os.mkdir(lib_platform.path_userhome + "/PyXes/pies")
                    lang01 = open(lib_platform.path_userhome + "/PyXes/pies/lang.pie", 'w')
                    if lang_ask == '1':
                        lang01.write('rus')
                    elif lang_ask == '2':
                        lang01.write('eng')
                    else:
                        pass
                    lang01.close()
                    lang01 = open(lib_platform.path_userhome + "/PyXes/pies/lang.pie", 'r')
                    lang = lang01.read()




        if lang == 'rus': #Тут русский | Russian here



            def runfile(x):
                    try:
                        os.startfile(x)
                    except:
                            print(x + " не команда и не исполняемый файл")

            def file(arg):
                if name == 'nt:':
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
                            save = input("\n\nСохранить изменения?\n (y/n)> ")
                            if save == 'y':
                                fl = open(filename, 'w', encoding='utf-8')
                                fl.writelines("%s" % inp)
                                fl.close()
                            elif save == 'n':
                                pass
                    except PermissionError:
                        print("[ALERT] - Плохой путь к файлу")

                    except UnicodeDecodeError:
                        print("[ALERT] - Ошибка юникода")
                    except FileNotFoundError:
                            print("Файл " + arg + " не может быть найден или редактирован")
                else:
                    os.system('nano ' + arg)

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

                if lex == 'help' or lex == 'HELP':
                    if arg == '--say':
                        print("SAY - Команда для вывода текста/математического действия на экран\nТекст или математическое действие указывать как аргумент\n\n")
                    elif arg == '--clear':
                        print("CLEAR - Команда для отчистки экрана\n\n")
                    elif arg == '--ls':
                        print("LS - Команда для просмотра содержимого директории. Если объект выделен зеленым, значит это директория.n\n")
                    elif arg == '--wia':
                        print("WIA - Команда для вывода текущего пути\n\n")
                    elif arg == '--':
                        print("CD - Команда для смены директории\nИмя директории указывать как аргумент\n\n")
                    elif arg == '--crctl':
                        print("MKDIR - Команда для создания директории\nИмя директории указывать как аргумент\n\n")
                    elif arg == '--rmctl':
                        print("RMDIR - Команда для удаления директории\nИмя директории указывать как аргумент\n\n")
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
                        print("<MKDIR    > создать директорию")
                        print("<RMDIR    > удалить директорию")
                        print("<RM       > удалить выбранный файл")
                        print("<FILE     > открыть текстовый редактор")
                        print("<TOUCH    > создать файл без редактирования")
                        print("<CAT      > вывести содержимое файла")
                        print("<CP       > скопировать файл в какое-то место или файл")
                        print('<WGET     > скачать файл из интернета')
                        print("<VER      > просмотреть версию терминала")
                elif lex.lower() == 'say':
                    try:
                        print(eval(arg))
                    except SyntaxError:
                        print(arg)
                    except ZeroDivisionError:
                        print("На ноль делить нельзя")

                    except NameError:
                        print(arg)

                elif lex.lower() == 'ls':
                    try:
                        print((special[6]*8) + special[3])
                        for i in os.listdir("."):
                            if os.path.isdir(i):
                                print("\t" + special[4], Back.GREEN + i)
                            else:
                                print("\t" + special[4], i)
                        print("")
                    except PermissionError:
                        print('Мне отказано в доступе')

                elif lex.lower() == 'wia':
                    print(os.getcwd())
                elif lex.lower() == 'clear':
                    clear()

                elif lex.lower() == 'cd':
                        if arg == '~':
                            os.chdir(lib_platform.path_userhome)
                        else:
                            try:
                                os.chdir(arg)
                            except FileNotFoundError:
                                print("Директория " + arg + " не найдена")

                            except OSError:
                                print("Недостаточно аргументов")
                            except:
                                print("Произошла непредвиденная ошибка :/")


                elif lex.lower() == 'mkdir':
                    try:
                        os.mkdir(arg)
                    except OSError:
                        print("Директория не может быть названа " + arg)

                elif lex.lower() == 'rmdir':
                        try:
                                shutil.rmtree(arg)
                        except FileNotFoundError:
                            print("Директория " + arg + " не найдена")

                        except OSError:
                                print("Директория не может быть названа " + arg)

                elif lex.lower() == 'file':
                    file(arg)
                elif lex.lower() == 'cat':
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
                elif lex.lower() == 'rm':
                        try:
                                os.remove(arg)
                        except FileNotFoundError:
                            print("Файл " + arg + " не найден")



                elif lex.lower() == 'touch':
                    try:
                        with open(arg, 'w') as lol1:
                            lol1.close()
                    except FileNotFoundError:
                        print("Файл " + arg + " не найден")



                elif lex.lower() == 'cp':
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


                elif lex.lower() == 'wget':
                    print("Пытаюсь скачать файл...\n")
                    try:
                        wget.download(arg)
                        print("\nФайл скачен!\n")
                    except:
                        print("\nНе удалось скачать файл. Возможно он повреждён или у вас нет подключения к интернету\n")





                    

                elif lex.lower() == 'ver':
                #     print("""
                # |OpenSource                         |
                # |PyXe (Python eXecution environment)|
                # |Сделано Space Core                 |

                # __________________________
                #          Версия """ + ver + "\n\n")
                    print("\n\n                " + special[2] + (special[6]*35) + special[3] + """
                │OpenSource                         │
                │PyXe (Python eXecution environment)│
                │Сделано Space Core                 │
                """
                + special[0] + (special[6]*35) + special[1] + "\n   \tВерсия ~-~ " + ver)


                elif lex.lower() == 'exit':
                    print("Выход...\nПока! Хорошего дня! :)\n\n")
                    sys.exit()

                else:
                    try:
                        print(eval(arg))
                    except SyntaxError:
                        try:
                            runfile(user)
                        except NameError():
                            print("Ошибка имени. Возможно, при попытке открыть предположительный файл с именем " + arg + ", PyXe ужаснулся, ведь этот файл не найден")
                        except:
                            print("Произошла неизвестная ошибка :/")
            
            while True:


                cursor = (Fore.RED + lib_platform.username + ":(" + os.getcwd() + ")" + Fore.RESET + "\n#: ")

                user = input(cursor)
                if lexer(user): break


        elif lang == 'eng': #English here | Тут английский

            def runfile(x):
                    try:
                        os.startfile(x)
                    except:
                        print(x + " is not a command or an executable")

            def file(arg):
                if name == 'nt':
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
                else:
                    os.system('nano ' + arg)
        




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

                if lex == 'help' or lex == 'HELP':
                    if arg == '--say':
                        print("SAY - Command for displaying text/math on the screen\nSpecify text or mathematical action as an argument\n\n")
                    elif arg == '--clear':
                        print("CLEAR - Command to clear the screen\n\n")
                    elif arg == '--ls':
                        print("LS - Command to view the contents of a directory. If the object is highlighted in green, then this is a directory\n\n")
                    elif arg == '--wia':
                        print("WIA - Command to display the current path\n\n")
                    elif arg == '--':
                        print("CD - Command to change directory\nDirectory name as an argument\n\n")
                    elif arg == '--crctl':
                        print("MKDIR - Command to create a directory\nDirectory name as an argument\n\n")
                    elif arg == '--rmctl':
                        print("RMDIR - Command to remove a directory\nDirectory name as an argument\n\n")
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
                        print("<MKDIR    > create a directory")
                        print("<RMDIR    > delete directory")
                        print("<RM       > delete selected file")
                        print("<FILE     > open text editor")
                        print("<TOUCH    > create file without editing")
                        print("<CAT      > output the contents of the file")
                        print("<CP       > copy the file to some location or file")
                        print('<WGET     > download file from internet')
                        print("<VER      > view terminal version")
                elif lex.lower() == 'say':
                    try:
                        print(eval(arg))
                    except SyntaxError:
                        print(arg)
                    except ZeroDivisionError:
                        print("Can't divide by zero")
                    except NameError:
                        print(arg)

                elif lex.lower() == 'ls':
                    try:
                        print((special[6]*8) + special[3])
                        for i in os.listdir("."):
                            if os.path.isdir(i):
                                print("\t" + special[4], Back.GREEN + i)
                            else:
                                print("\t" + special[4], i)
                        print("")
                    except PermissionError:
                        print('I was denied access')

                elif lex.lower() == 'wia':
                    print(os.getcwd())
                elif lex.lower() == 'clear':
                    clear()

                elif lex.lower() == 'cd':
                        if arg == '~':
                            os.chdir(lib_platform.path_userhome)
                        else:
                            try:
                                os.chdir(arg)
                            except FileNotFoundError:
                                print("Directory " + arg + " not found")
                            except:
                                print("An unexpected error has occurred :/")

                elif lex.lower() == 'mkdir':
                    try:
                        os.mkdir(arg)
                    except OSError:
                        print("Directory cannot be named " + arg)
                elif lex.lower() == 'rmdir':
                        try:
                                shutil.rmtree(arg)
                        except FileNotFoundError:
                            print("Directory " + arg + " not found")

                        except OSError:
                                print("Directory cannot be named " + arg)
                elif lex.lower() == 'file':
                    file(arg)
                elif lex.lower() == 'cat':
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
                elif lex.lower() == 'rm':
                        try:
                                os.remove(arg)
                        except FileNotFoundError:
                            print("File " + arg + " not found")



                elif lex.lower() == 'touch':
                    try:
                        with open(arg, 'w') as lol1:
                            lol1.close()
                    except FileNotFoundError:
                        print("File " + arg + " not found")

                    

                elif lex.lower() == 'cp':
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
                    print("Trying to download a file...\n")
                    try:
                        wget.download(arg)
                        print("\nFile downloaded!\n")
                    except:
                        print("\nFailed to download file. Maybe it's damaged or you don't have an internet connection\n")
                    

                elif lex.lower() == 'ver':
                #     print("""
                # |OpenSource                         |
                # |PyXe (Python eXecution environment)|
                # |Made by Space Core                 |
            
                # __________________________
                #      Version """ + ver + "\n")
                    print("\n\n                " + special[2] + (special[6]*35) + special[3] + """
                │OpenSource                         │
                │PyXe (Python eXecution environment)│
                │Made by Space Core                 │
                """
                + special[0] + (special[6]*35) + special[1] + "\n   \tVersion ~-~ " + ver)

                elif lex.lower() == 'exit':
                    print("Exit...\nBye! Have a good day! :)\n\n")
                    sys.exit()

                else:
                    try:
                        print(eval(arg))
                    except SyntaxError:
                        try:
                            runfile(user)
                        except NameError():
                            print("Name error. Perhaps when trying to open a supposed file called " + arg + ", PyXe was horrified because this file was not found")
                        except:
                            print('An unknown error has occurred :/')
        
            while True:
                cursor = (Fore.RED + lib_platform.username + ":(" + os.getcwd() + ")" + Fore.RESET + "\n#: ")


                user = input(cursor)
                if lexer(user): break





    except NameError:
        print(":P")

    except AttributeError:
        if lang == 'rus':
            print("Некорректный ввод >:(")
        elif lang == 'eng':
            print("Invalid input >:(")
