from tkinter import messagebox

class rus():
    def no_file_error(self):
        messagebox.showerror('Ошибка', message=('Файл ' + self + ' не найден'))

    def cant_read_error(self):
        messagebox.showerror('Ошибка', message=('Файл ' + self + ' не может быть найден, прочитан или отредактирован'))

    def not_command(self):
        messagebox.showerror('Ошибка', message=(self + ' не команда и не исполняемый файл'))

    def not_exist(self):
        messagebox.showerror('Ошибка', message=('Файл ' + self + ' уже существует'))

    def dir_is_not_exist(self):
        messagebox.showerror('Ошибка', message=('Директория ' + self + ' не найдена'))

    def dir_name_error(self):
        messagebox.showerror('Ошибка',  message=('Директория не может быть названа: ' + self))

    def zero_dev():
        messagebox.showerror('Ошибка', "Делить на ноль нельзя")

    def idk():
        messagebox.showerror('Ошибка', 'Произошла неизвестная ошибка :/')

class eng():
    def no_file_error(self):
        messagebox.showerror('Error', message=('File ' + self + ' not found'))

    def cant_read_error(self):
        messagebox.showerror('Error', message=('File ' + self + ' could not be found, read or edited'))

    def not_command(self):
        messagebox.showerror('Error', message=(self + ' is not a command or an executable'))

    def not_exist(self):
        messagebox.showerror('Error', message=('File ' + self + ' already exists'))

    def dir_is_not_exist(self):
        messagebox.showerror('Error', message=('Directory ' + self + ' not found'))

    def dir_name_error(self):
        messagebox.showerror('Error',  message=('The directory cannot be named:' + self))

    def zero_dev():
        messagebox.showerror('Error', "Can't divide by zero")

    def idk():
        messagebox.showerror('Error', 'An unknown error has occurred :/')
