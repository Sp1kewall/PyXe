import os, sys


if os.path.isfile('settings/lang.txt'):
    pass
else:
    lang_ask = input("""
Choose your language:
Выберите свой язык:

\t 1.Русский (Russian)
\t 2.English (Английский)
$:""")

    lang01 = open('settings/lang.txt', 'w')
    if lang_ask == '1':
        lang01.write('rus')
    elif lang_ask == '2':
        lang01.write('eng')
    lang01.close()

os.chdir('st')
if os.name == 'nt':
    os.startfile('terminal.py')
    sys.exit()
else:
    if lang_ask == '2':
        input('Now you need to run the terminal.py file in the "st" directory')
    elif lang_ask == '1':
        input('Теперь вам нужно запустить файл terminal.py в директории "st"')
