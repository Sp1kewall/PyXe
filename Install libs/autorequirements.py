'This module is made to improve the installation of uninstalled modules, as well as to demonstrate the lib folder for PyXe'
import os, sys
from os import name
def clear():
    c = 'clear'
    if name == 'nt': c = 'cls'
    os.system(c)



requirements = """
lib_platform
colorama
wget"""

def install_req(language, requirements):
    if language == 'eng':
        ask = input("Modules are not installed or are not working correctly. Press Ctrl + C at startup to install all modules\nOr install them now\nInstall? [y/n] $:")
        if ask == 'y' or ask == 'Y':
            print("Installing modules...")
            if name == 'nt':
                clear()
                req = open("requirements.txt", "w")
                req.writelines(requirements)
                req.close()
                os.system("pip install -r requirements.txt")
                os.remove("requirements.txt")
                clear()
                input("[  OK  ]  All modules are installed!\n")
            elif name == 'posix':
                req = open("requirements.txt", "w")
                req.writelines(requirements)
                req.close()
                clear()
                var1 = input("Install pip?\n(y/n)$:")
                if var1 == 'y' or var1 == "Y":
                    os.system("sudo apt install python3-pip")
                else:
                    pass
                clear()
                os.system("pip3 install -r requirements.txt")
                os.remove("requirements.txt")
                clear()
                input("[  OK  ]  All modules are installed!\n")
        elif ask == 'n' or ask == 'N':
            sys.exit()
        else:
            print("Are you serious?")
    
    elif language == 'rus':
        ask = input("Модули не установлены или работают не правильно. Нажмите при запуске Ctrl + C для установки всех модулей\nИли установите их сейчас\nУстановить? [y/n] $:")
        if ask == 'y' or ask == 'Y':
            print("Установка модулей...")
            if name == 'nt':
                clear()
                req = open("requirements.txt", "w")
                req.writelines(requirements)
                req.close()
                os.system("pip install -r requirements.txt")
                os.remove("requirements.txt")
                input("[  OK  ]  Все модули установлены!\n")
                sys.exit()
            elif name == 'posix':
                req = open("requirements.txt", "w")
                req.writelines(requirements)
                req.close()
                clear()
                var1 = input("Установить pip?\n(y/n)$:")
                if var1 == 'y' or var1 == "Y":
                    os.system("sudo apt install python3-pip")
                else:
                    pass
                os.system("pip3 install -r requirements.txt")
                os.remove("requirements.txt")
                clear()
                input("[  OK  ]  Все модули установлены!\n")
                sys.exit()
        elif ask == 'n' or ask == 'N':
            sys.exit()
        else:
            print("Ты серьёзно?")

    else:
        ask = input("Modules are not installed or are not working correctly. Press Ctrl + C at startup to install all modules\nOr install them now\nInstall? [y/n] $:")
        if ask == 'y' or ask == 'Y':
            print("Installing modules...")
            if name == 'nt':
                clear()
                req = open("requirements.txt", "w")
                req.writelines(requirements)
                req.close()
                os.system("pip install -r requirements.txt")
                os.remove("requirements.txt")
                clear()
                input("[  OK  ]  All modules are installed!\n")
            elif name == 'posix':
                req = open("requirements.txt", "w")
                req.writelines(requirements)
                req.close()
                clear()
                var1 = input("Install pip?\n(y/n)$:")
                if var1 == 'y' or var1 == "Y":
                    os.system("sudo apt install python3-pip")
                else:
                    pass
                clear()
                os.system("pip3 install -r requirements.txt")
                os.remove("requirements.txt")
                clear()
                input("[  OK  ]  All modules are installed!\n")
        elif ask == 'n' or ask == 'N':
            sys.exit()
        else:
            print("Are you serious?")


install_req("eng", requirements)