"This is my first module for Python!!!! WOW!!!!!"


import os, sys
from os import name
try:
    from colorama import Fore, Back, init
    init(autoreset=True)
    def red():
        print(Fore.RED + Back.RED + "█", end='')

    def blue():
        print(Fore.BLUE + Back.BLUE + "█", end='')

    def white():
        print(Fore.WHITE + Back.WHITE + "█", end='')

    def black():
        print(Fore.BLACK + Back.BLACK + "█", end='')

    def green():
        print(Fore.GREEN + Back.GREEN + "█", end='')

    def yellow():
        print(Fore.YELLOW + Back.YELLOW + "█", end='')

    def magenta():
        print(Fore.MAGENTA + Back.MAGENTA + "█", end='')

    def cyan():
        print(Fore.CYAN + Back.CYAN + "█", end='')

    def lightblack():
        print(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX + "█", end='')

    def lightblue():
        print(Fore.LIGHTBLUE_EX + Back.LIGHTBLUE_EX + "█", end='')

    def lightcyan():
        print(Fore.LIGHTCYAN_EX + Back.LIGHTCYAN_EX + "█", end='')

    def lightgreen():
        print(Fore.LIGHTGREEN_EX + Back.LIGHTGREEN_EX + "█", end='')

    def lightmagenta():
        print(Fore.LIGHTMAGENTA_EX + Back.LIGHTMAGENTA_EX + "█", end='')

    def lightred():
        print(Fore.LIGHTRED_EX + Back.LIGHTRED_EX + "█", end='')

    def lightwhite():
        print(Fore.LIGHTWHITE_EX + Back.LIGHTWHITE_EX + "█", end='')

    def lightyellow():
        print(Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX + "█", end='')

    def enter():
        print("\n", end='')

    def line():
        print('-', end='')
        
    def present(filename):
        print_picture = open(filename, 'r', encoding='utf-8')
        a = print_picture.read()
        if 'spix_ez' in a:
            for i in a:
                if i == 'r' or i == 'R':
                            red()
                elif i == 'b' or i =='B':
                            blue()
                elif i == 'g' or i == 'G':
                            green()
                elif i == '\n':
                            enter()
                elif i == 'w' or i == 'W':
                            white()
                elif i == 'y' or i == 'Y':
                            yellow()
                elif i == 'v' or i == 'V':
                            black()
                elif i == '-':
                    line()
                else:
                    print("", end='')
            print_picture.close()
            print('\n\n')

        elif 'spix_tc' in a:
            for i in a:
                if i == 'w':
                    white()
                elif i == 'W':
                    lightwhite()
                elif i == 'v':
                    black()
                elif i == 'V':
                    lightblack()
                elif i == '-':
                    line()
                elif i == '\n':
                    print("\n", end='')
                else:
                    pass

        else:
            for i in a:
                if i == 'r':
                            red()
                elif i == 'b':
                            blue()
                elif i == 'g':
                            green()
                elif i == 'e' or i == 'E' or i == '\n':
                            enter()
                elif i == 'w':
                            white()
                elif i == 'y':
                            yellow()
                elif i == 'm':
                            magenta()
                elif i == 'c':
                            cyan()
                elif i == 'v':
                            black()
                elif i == 'R':
                            lightred()
                elif i == 'B':
                            lightblue()
                elif i == 'G':
                            lightgreen()
                elif i == 'W':
                            lightwhite()
                elif i == 'Y':
                            lightyellow()
                elif i == 'M':
                            lightmagenta()
                elif i == 'V':
                            lightblack()
                elif i == '-':
                    line()
                else:
                        print("", end='')
            print_picture.close()
            print('\n\n')

except ModuleNotFoundError:
        if name == 'posix':
            ask = input('Install pip?\n$:')
            if ask == 'y' or ask == 'Y':
                os.system('sudo apt install python3-pip')
            else:
                pass
            os.system('pip install colorama')
            os.system('clear')
        elif name == 'nt':
            os.system('pip install colorama')
            os.system('cls')
        sys.exit()


if __name__ == '__main__':
    present("test.spr")
