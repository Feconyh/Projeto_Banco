import tkinter as tk
from tkinter import ttk


# Parte do Banco

class Client:
    Users = []

    def __init__(self, name, cpf, age, phonenumber, accountnumber, password, balance):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.phonenumber = phonenumber

        self.accountnumber = accountnumber
        self.password = password
        self.balance = balance
        self.history = []

    def deposit(self, amount):

        if amount not in '1234568790.':
            return False
        elif amount <= 0:
            return False
        else:
            self.balance += amount
            return True

    def withdrawal(self, amount):

        if amount not in '1234568790.':
            return False
        elif amount <= 0:
            return False
        elif amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def transfer(self, amount, subject):
        if amount not in '1234568790.':
            return False
        elif amount <= 0:
            return False
        elif amount > self.balance:
            return False
        else:
            subject.balance += amount
            self.balance -= amount
            return True

    def history(self, transfer, amount, who):
        if transfer == 1:
            self.history.append(f'Deposit of {amount}')
        if transfer == 2:
            self.history.append(f'Withdrawal of {amount}')
        if transfer == 3:
            self.history.append(f'Transfer of {amount} to acount{who}')

# UI/HUD stuff


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('720x1000+610+0')
        self.title('Bank App')
        self.resizable(False, False)

        self.curr_screen = None

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def screen_one(self):
        self.clear()
        self.curr_screen = LoginScreen(self, True)

    def screen_two(self):
        self.clear()
        self.curr_screen = UserLoggedScreen(self, True)

    def screen_three(self):
        self.clear()
        self.curr_screen = CreditsScreen(self, True)

    def screen_four(self):
        self.clear()
        self.curr_screen = DepositScreen(self, True)

    def screen_five(self):
        self.clear()
        self.curr_screen = WithdrawalScreen(self, True)

    def screen_six(self):
        self.clear()
        self.curr_screen = TransferScreen(self, True)


class LoginScreen(ttk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:
            self.pack()
            lbl = ttk.Label(self, text='Tela 1')
            lbl.pack()
            bttn = ttk.Button(self, text='Mudar tela', command=app.screen_two)
            bttn.pack()


class UserLoggedScreen(ttk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:
            self.pack()
            lbl = ttk.Label(root, text='Tela 2')
            lbl.pack()
            bttn = ttk.Button(self, text='Mudar tela', command=app.screen_three)
            bttn.pack()


class CreditsScreen(ttk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:
            self.pack()
            lbl = ttk.Label(root, text='Tela 3')
            lbl.pack()
            bttn = ttk.Button(self, text='Mudar tela', command=app.screen_four)
            bttn.pack()


class DepositScreen(ttk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:
            self.pack()
            lbl = ttk.Label(root, text='Tela 4')
            lbl.pack()
            bttn = ttk.Button(self, text='Mudar tela', command=app.screen_five)
            bttn.pack()


class WithdrawalScreen(ttk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:
            self.pack()
            lbl = ttk.Label(root, text='Tela 5')
            lbl.pack()
            bttn = ttk.Button(self, text='Mudar tela', command=app.screen_six)
            bttn.pack()


class TransferScreen(ttk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:
            self.pack()
            lbl = ttk.Label(root, text='Tela 6')
            lbl.pack()
            bttn = ttk.Button(self, text='Mudar tela', command=app.screen_one)
            bttn.pack()


if __name__ == '__main__':
    app = App()
    app.screen_one()
    app.mainloop()