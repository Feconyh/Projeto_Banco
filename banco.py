import tkinter as tk
from tkinter import *
import HelpPlace

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

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("720x1000+610+0")
        self.title('Bank App')
        self.iconbitmap(default="image\player.ico")
        self.resizable(width=False, height=False)

        self.curr_screen = None
        
        self.bind('<Button-1>', HelpPlace.inicio_place)
        self.bind('<ButtonRelease-1>', lambda arg: HelpPlace.fim_place(arg, self))
        self.bind('<Button-2>', lambda arg: HelpPlace.para_geometry(self))

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
        self.curr_screen = AdmLoggedScreen(self, True)
#
#    def screen_four(self):
#        self.clear()
#        self.curr_screen = DepositScreen(self, True)
#
#    def screen_five(self):
#        self.clear()
#        self.curr_screen = WithdrawalScreen(self, True)
#
#    def screen_six(self):
#        self.clear()
#        self.curr_screen = TransferScreen(self, True)  

class LoginScreen(tk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:

            # importação de imagem da tela de login
            self.tumb_one = PhotoImage(file="image/Tumb.png")
            self.entry = PhotoImage(file='image/entry.png')
            self.login = PhotoImage(file='image/login.png')
            self.user = PhotoImage(file='image/usuario.png')
            self.password = PhotoImage(file='image/senha.png')
            self.button_login = PhotoImage(file='image/button_login.png')

            root.configure(bg='#0231a0')

            self.tumb_log = tk.Label(root, image=self.tumb_one)
            self.tumb_log.place(width=360, height=1000, x=360, y=0)

            self.login_log = tk.Label(root, image=self.login)
            self.login_log.place(width=175, height=69, x=30, y=36)

            self.user_log = tk.Label(root, image=self.user)
            self.user_log.place(width=180, height=50, x=30, y=260)

            self.password_log = tk.Label(root, image=self.password)
            self.password_log.place(width=140, height=50, x=30, y=400)

            
            self.user_ent = tk.Entry(root, highlightthickness=2)
            self.user_ent.place(width=300, height=40, x=30, y=320)
            self.user_ent.config(highlightbackground = "#f65a05", bg= "#0231a0", fg='#ffffff')

            self.password_ent = tk.Entry(root, highlightthickness=2)
            self.password_ent.place(width=300, height=40, x=30, y=460)
            self.password_ent.config(highlightbackground = "#f65a05", bg= "#0231a0", fg='#ffffff', show='*')

            self.login_btn = tk.Button(root, bd=0, image=self.button_login, command=app.screen_two)
            self.login_btn.place(width=300, height=118, x=30, y=520)
   
class UserLoggedScreen(tk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:

#            self.pack()
#            lbl = tk.Label(root, text='Tela 2')
#            lbl.pack()
#            bttn = tk.Button(root, text='Mudar tela', command=app.screen_three)
#            bttn.pack()

            # importação de imagem da tela de User
            self.header = PhotoImage(file='image/header.png')
            self.historic = PhotoImage(file='image/historic.png')

            self.extract = PhotoImage(file='image/extrato.png')
            self.deposit = PhotoImage(file='image/deposit.png')
            self.withdrawal = PhotoImage(file='image/withdrawal.png')
            self.transfer = PhotoImage(file='image/transfer.png')
            self.exit = PhotoImage(file='image/exit.png')

            self.cuie = PhotoImage(file='image/cuie.png')

            self.bottom_bar = PhotoImage(file='image/bottom_bar.png')

            root.configure(bg='#ec7001')

            self.header_user = tk.Label(root, bd=0, image=self.header)
            self.header_user.place(width=720, height=200, x=0, y=0)

            self.historic_user = tk.Button(root, bd=0, image=self.historic, command=app.screen_three)
            self.historic_user.place(width=720, height=100, x=0, y=200)


            self.extract_btn = tk.Button(root, bd=0, image=self.extract)
            self.extract_btn.place(width=225, height=140, x=50, y=340)

            self.deposit_btn = tk.Button(root, bd=0, image=self.deposit)
            self.deposit_btn.place(width=225, height=140, x=410, y=340)

            self.withdrawal_btn = tk.Button(root, bd=0, image=self.withdrawal)
            self.withdrawal_btn.place(width=225, height=140, x=50, y=520)

            self.transfer_btn = tk.Button(root, bd=0, image=self.transfer)
            self.transfer_btn.place(width=225, height=140, x=410, y=520)

            self.exit_btn = tk.Button(root, bd=0, image=self.exit, command=app.screen_one)
            self.exit_btn.place(width=225, height=140, x=50, y=700)

            self.cuie_user = tk.Label(root, bd=0, image=self.cuie)
            self.cuie_user.place(width=225, height=200, x=410, y=700)

            self.bottom_bar_user = tk.Label(root, bd=0, image=self.bottom_bar)
            self.bottom_bar_user.place(width=720, height=100, x=0, y=900)

class AdmLoggedScreen(tk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:

            # importação de imagem da tela de Adm
            self.header = PhotoImage(file='image/header.png')
            self.historic = PhotoImage(file='image/historic.png')

            self.extract = PhotoImage(file='image/extrato.png')
            self.deposit = PhotoImage(file='image/deposit.png')
            self.withdrawal = PhotoImage(file='image/withdrawal.png')
            self.transfer = PhotoImage(file='image/transfer.png')
            self.exit = PhotoImage(file='image/exit.png')

            self.adm = PhotoImage(file='image/adm_settings.png')

            self.bottom_bar = PhotoImage(file='image/bottom_bar.png')

            root.configure(bg='#ec7001')

            self.header_user = tk.Label(root, bd=0, image=self.header)
            self.header_user.place(width=720, height=200, x=0, y=0)

            self.historic_user = tk.Button(root, bd=0, image=self.historic)
            self.historic_user.place(width=720, height=100, x=0, y=200)


            self.extract_btn = tk.Button(root, bd=0, image=self.extract)
            self.extract_btn.place(width=225, height=140, x=50, y=340)

            self.deposit_btn = tk.Button(root, bd=0, image=self.deposit)
            self.deposit_btn.place(width=225, height=140, x=410, y=340)

            self.withdrawal_btn = tk.Button(root, bd=0, image=self.withdrawal)
            self.withdrawal_btn.place(width=225, height=140, x=50, y=520)

            self.transfer_btn = tk.Button(root, bd=0, image=self.transfer)
            self.transfer_btn.place(width=225, height=140, x=410, y=520)

            self.exit_btn = tk.Button(root, bd=0, image=self.exit, command=app.screen_one)
            self.exit_btn.place(width=225, height=140, x=50, y=700)

            self.adm_settings = tk.Button(root, bd=0, image=self.adm)
            self.adm_settings.place(width=225, height=140, x=410, y=700)

            self.bottom_bar_user = tk.Label(root, bd=0, image=self.bottom_bar)
            self.bottom_bar_user.place(width=720, height=100, x=0, y=900) 
    
if __name__ == "__main__":

    app = App()
    app.screen_one()
    app.mainloop()