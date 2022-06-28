from re import A
import tkinter as tk
from tkinter import *

import HelpPlace
import random

class Client:
    users = []

    def __init__(self, name, cpf, age, phonenumber,admin = False,accountnumber=0,password=0,balance=0):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.phonenumber = phonenumber
        self.admin = admin

        self.accountnumber = Users.usercount
        self.password = password
        if password == 0:
            self.password = random.randint(0,1000)
        self.balance = balance
        self.history = []

    def tran(self, transfer, amount, who=None):
        if transfer == 1:
            self.history.append(f'Deposit of {amount}')
        if transfer == 2:
            self.history.append(f'Withdrawal of {amount}')
        if transfer == 3:
            self.history.append(f'Transfer of {amount} to acount{who}')

    def deposit(self, amount):
        
        try:
            amount = int(amount)
            if amount <= 0:
                return False
            else:
                self.tran(1,amount)
                self.balance += amount
                return True
        except:
            return False

    def withdrawal(self, amount):
        try:
            amount = int(amount)
            if amount <= 0 or  amount > self.balance:
                return False
            else:
                self.tran(2,amount)
                self.balance -= amount
                return True
        except:
            return False

    def transfer(self, amount, subject):
        try:
            print('try')
            amount = int(amount)
            subject = int(subject)
            user_id = Users.userwheel[subject]  

            if self.accountnumber == user_id.accountnumber or amount <= 0 or amount > self.balance:
                return False
            else:
                self.tran(3,str(amount),str(subject))
                user_id.balance += amount
                self.balance -= amount
                return True
        except:
            return False

class Users:
    usercount = 0
    userwheel = []

    @staticmethod
    def create_user(name, cpf, age, phonenumber,admin,accountnumber=0, password=0, balance=0):
        Users.userwheel.append(Users.usercount)
        Users.userwheel[Users.usercount] = Client(name, cpf, age, phonenumber, admin, accountnumber, password, balance)
        Users.usercount += 1

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("720x1000+610+0")
        def move_window(event):
                self.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
        self.overrideredirect(False)

        self.title('Bank App')
        self.iconbitmap(default="image\player.ico")
        self.resizable(width=False, height=False)

        self.curr_screen = None

        #self.bind('<B1-Motion>', move_window)

        self.bind('<Button-1>', HelpPlace.inicio_place)
        self.bind('<ButtonRelease-1>', lambda arg: HelpPlace.fim_place(arg, self))
        self.bind('<Button-2>', lambda arg: HelpPlace.para_geometry(self))

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def screen_one(self):
        self.clear()
        self.curr_screen = LoginScreen(self,True)

    def screen_two(self,user_id):
        self.clear()
        self.curr_screen = UserLoggedScreen(self, user_id, True)
        
    def screen_three(self,user_id):

        self.clear()
        self.curr_screen = AdmLoggedScreen(self, user_id, True)

    def screen_four(self):
        self.clear()
        self.curr_screen = RegisterScreen(self, True)

    def screen_five(self,user_id):
        self.clear()
        self.curr_screen = DepositScreen(self, user_id, True)

    def screen_six(self,user_id):
        self.clear()
        self.curr_screen = WithdrawalScreen(self, user_id,True)

    def screen_seven(self,user_id):
        self.clear()
        self.curr_screen = TransferScreen(self, user_id, True)

class LoginScreen(tk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:

            # importação de imagem da tela de login
            self.backgournd_login = PhotoImage(file="image/background_login.png")
            self.button_login = PhotoImage(file='image/button_login.png')

            self.background = tk.Label(root, image=self.backgournd_login)
            self.background.place(width=720, height=1000, x=0, y=0)

            self.user_ent = tk.Entry(root)
            self.user_ent.place(width=275, height=50, x=20, y=240)
            self.user_ent.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')

            self.password_ent = tk.Entry(root)
            self.password_ent.place(width=275, height=50, x=20, y=360)
            self.password_ent.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff', show='*')

            self.login_btn = tk.Button(root, bd=0, image=self.button_login, command=self.verify_login)
            self.login_btn.place(width=230, height=100, x=12, y=510)

    def verify_login(self):
        for i in range(Users.usercount):

            if self.user_ent.get() == Users.userwheel[i].name:
                if self.password_ent.get() == Users.userwheel[i].password:
                    if Users.userwheel[i].admin == False:
                        app.screen_two(i)
                    elif Users.userwheel[i].admin == True:
                        app.screen_three(i)

class UserLoggedScreen(tk.Frame):
    def __init__(self, root, user_id, render=False):
        super().__init__(root)
        if render:

            self.root = root
            self.user = Users.userwheel[user_id]
            self.user_id = user_id

            # importação de imagem da tela de user
            self.header = PhotoImage(file='image/header.png')
            self.historic = PhotoImage(file='image/historic.png')

            self.extract = PhotoImage(file='image/extrato.png')
            self.deposit = PhotoImage(file='image/deposit.png')
            self.withdrawal = PhotoImage(file='image/withdrawal.png')
            self.transfer = PhotoImage(file='image/transfer.png')
            self.exit = PhotoImage(file='image/exit.png')

            self.olho = PhotoImage(file='image/olho.png')

            self.cuie = PhotoImage(file='image/cuie.png')

            self.bottom_bar = PhotoImage(file='image/bottom_bar.png')

            root.configure(bg='#ec7001')

            self.header_user = tk.Label(root, bd=0, image=self.header)
            self.header_user.place(width=720, height=200, x=0, y=0)

            self.historic_user = tk.Button(root, bd=0, image=self.historic, command='')
            self.historic_user.place(width=720, height=100, x=0, y=200)

            self.extract_btn = tk.Button(root, bd=0, image=self.extract)
            self.extract_btn.place(width=225, height=140, x=50, y=340)

            self.deposit_btn = tk.Button(root, bd=0,image=self.deposit, command=self.botao_deposito)
            self.deposit_btn.place(width=225, height=140, x=410, y=340)

            self.withdrawal_btn = tk.Button(root, bd=0, image=self.withdrawal, command=self.botao_withdrawal)
            self.withdrawal_btn.place(width=225, height=140, x=50, y=520)

            self.transfer_btn = tk.Button(root, bd=0, image=self.transfer, command=self.botao_transfer)
            self.transfer_btn.place(width=225, height=140, x=410, y=520)

            self.exit_btn = tk.Button(root, bd=0, image=self.exit, command=app.screen_one)
            self.exit_btn.place(width=225, height=140, x=50, y=700)

            self.cuie_user = tk.Label(root, bd=0, image=self.cuie)
            self.cuie_user.place(width=225, height=200, x=410, y=700)

            self.bottom_bar_user = tk.Label(root, bd=0, image=self.bottom_bar)
            self.bottom_bar_user.place(width=720, height=100, x=0, y=900)

            self.nome = Label(root,text = self.user.name)
            self.nome.place(width=172, height=26, x=290, y=30)
            self.nome.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')

            self.senha = Label(root,text = self.user.password)
            self.senha.place(width=103, height=40, x=607, y=128)
            self.senha.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')

            self.id = Label(root,text = self.user.accountnumber)
            self.id.place(width=134, height=35, x=578, y=84)
            self.id.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')
        
            self.saldo = Label(root,text = self.user.balance)
            self.saldo.place(width=205, height=55, x=15, y=127)
            self.saldo.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')

            self.hidden = True
            self.ocult = tk.Button(root, bd=0, image=self.olho, command=self.botao_saldo)
            self.ocult.place(width=75, height=50, x=224, y=130)

    def botao_deposito(self):
        app.screen_five(self.user_id)

    def botao_withdrawal(self):
        app.screen_six(self.user_id)

    def botao_transfer(self):
        app.screen_seven(self.user_id)

    def botao_saldo(self):
        if self.hidden == False:
            self.saldo = Label(self.root,text = self.user.balance)
            self.saldo.place(width=205, height=55, x=15, y=127)
            self.saldo.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')
            self.hidden = True

        elif self.hidden == True:
            self.show = Label(self.root,text='EasterEgg')
            self.show.place(width=205, height=55, x=15, y=127)
            self.show.configure(bg='#4b4e53', fg='#4b4e53')
            self.hidden = False


class AdmLoggedScreen(tk.Frame):
    def __init__(self, root, user_id, render=False):
        super().__init__(root)
        if render:

            self.root = root
            self.user = Users.userwheel[user_id]
            self.user_id = user_id

            # importação de imagem da tela de Adm
            self.header = PhotoImage(file='image/header.png')
            self.historic = PhotoImage(file='image/historic.png')

            self.extract = PhotoImage(file='image/extrato.png')
            self.deposit = PhotoImage(file='image/deposit.png')
            self.withdrawal = PhotoImage(file='image/withdrawal.png')
            self.transfer = PhotoImage(file='image/transfer.png')
            self.exit = PhotoImage(file='image/exit.png')

            self.olho = PhotoImage(file='image/olho.png')

            self.adm = PhotoImage(file='image/adm_settings.png')

            self.bottom_bar = PhotoImage(file='image/bottom_bar.png')

            root.configure(bg='#ec7001')

            self.header_user = tk.Label(root, bd=0, image=self.header)
            self.header_user.place(width=720, height=200, x=0, y=0)

            self.historic_user = tk.Button(root, bd=0, image=self.historic)
            self.historic_user.place(width=720, height=100, x=0, y=200)

            self.extract_btn = tk.Button(root, bd=0, image=self.extract)
            self.extract_btn.place(width=225, height=140, x=50, y=340)

            self.deposit_btn = tk.Button(root, bd=0, image=self.deposit, command=self.botao_deposito)
            self.deposit_btn.place(width=225, height=140, x=410, y=340)

            self.withdrawal_btn = tk.Button(root, bd=0, image=self.withdrawal, command= self.botao_withdrawal)
            self.withdrawal_btn.place(width=225, height=140, x=50, y=520)

            self.transfer_btn = tk.Button(root, bd=0, image=self.transfer, command=self.botao_transfer)
            self.transfer_btn.place(width=225, height=140, x=410, y=520)

            self.exit_btn = tk.Button(root, bd=0, image=self.exit, command=app.screen_one)
            self.exit_btn.place(width=225, height=140, x=50, y=700)

            self.adm_settings = tk.Button(root, bd=0, image=self.adm, command=app.screen_four)
            self.adm_settings.place(width=225, height=140, x=410, y=700)

            self.bottom_bar_user = tk.Label(root, bd=0, image=self.bottom_bar)
            self.bottom_bar_user.place(width=720, height=100, x=0, y=900) 

            self.nome = Label(root,text = self.user.name)
            self.nome.place(width=172, height=26, x=290, y=30)
            self.nome.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')

            self.senha = Label(root,text = self.user.password)
            self.senha.place(width=103, height=40, x=607, y=128)
            self.senha.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')

            self.id = Label(root,text = self.user.accountnumber)
            self.id.place(width=134, height=35, x=578, y=84)
            self.id.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')
        
            self.saldo = Label(root,text = self.user.balance)
            self.saldo.place(width=205, height=55, x=15, y=127)
            self.saldo.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')

            self.hidden = True
            self.ocult = tk.Button(root, bd=0, image=self.olho, command=self.botao_saldo)
            self.ocult.place(width=75, height=50, x=224, y=130)

    def botao_deposito(self):
        app.screen_five(self.user_id)

    def botao_withdrawal(self):
        app.screen_six(self.user_id)

    def botao_transfer(self):
        app.screen_seven(self.user_id)

    def botao_saldo(self):
        if self.hidden == False:
            self.saldo = Label(self.root,text = self.user.balance)
            self.saldo.place(width=205, height=55, x=15, y=127)
            self.saldo.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')
            self.hidden = True

        elif self.hidden == True:
            self.show = Label(self.root,text='EasterEgg')
            self.show.place(width=205, height=55, x=15, y=127)
            self.show.configure(bg='#4b4e53', fg='#4b4e53')
            self.hidden = False

    
class RegisterScreen(tk.Frame):
    def __init__(self, root, render=False):
        super().__init__(root)
        if render:

            # importação de imagem da tela de cadastro
            self.background_register = PhotoImage(file='image/background_register.png')
            self.button_create = PhotoImage(file='image/button_create.png')
            
            self.background = tk.Label(root, bd=0, image=self.background_register)
            self.background.place(width=720, height=1000, x=0, y=0)

            self.nome_ent = tk.Entry(root)
            self.nome_ent.place(width=360, height=42, x=228, y=233)
            self.nome_ent.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')
            
            self.cpf_ent = tk.Entry(root)
            self.cpf_ent.place(width=360, height=42, x=230, y=322)
            self.cpf_ent.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')

            self.idade_ent = tk.Entry(root)
            self.idade_ent.place(width=101, height=42, x=228, y=407)
            self.idade_ent.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')

            self.telefone_ent = tk.Entry(root)
            self.telefone_ent.place(width=361, height=45, x=228, y=499)
            self.telefone_ent.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')

            self.senha_ent = tk.Entry(root)
            self.senha_ent.place(width=361, height=43, x=228, y=592)
            self.senha_ent.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')

            self.create = tk.Button(root, bd=0, image=self.button_create,command=self.cadrastar)
            self.create.place(width=445, height=115, x=166, y=710)

    def cadrastar(self):

        Users.create_user(self.nome_ent.get(), self.cpf_ent.get(), self.idade_ent.get(), self.telefone_ent.get(),False,0,self.senha_ent.get())
        app.screen_two(Users.usercount-1)


class DepositScreen(tk.Frame):
    def __init__(self, root, user_id, render=False):
        super().__init__(root)
        if render:
            self.user = Users.userwheel[user_id]
            self.user_id = user_id

            self.background_register = PhotoImage(file='image/background_register.png')
            self.button_create = PhotoImage(file='image/button_create.png')
            
            #self.background = tk.Label(root, bd=0, image=self.background_register)
            #self.background.place(width=720, height=1000, x=0, y=0)

            self.saldo = Label(root, text=self.user.balance)
            self.saldo.place(width=205, height=55, x=15, y=127)
            self.saldo.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')

            self.quantia = tk.Entry(root)
            self.quantia.place(width=360, height=42, x=228, y=233)
            self.quantia.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')

            self.deposito = tk.Button(root, bd=0, image=self.button_create,command=self.deposit)
            self.deposito.place(width=445, height=115, x=166, y=710)

            self.back = tk.Button(root, bd=0, image=self.button_create,command=self.sair)
            self.back.place(width=365, height=97, x=176, y=890)
            
    def deposit(self):

        if self.user.deposit(self.quantia.get()) == True:
            print('foi de certo tudobom')
        else:
            print('algo deu errado na chamada')

    def sair(self):
        if self.user.admin == False:
            app.screen_two(self.user_id)
        elif self.user.admin == True:
            app.screen_three(self.user_id)


class WithdrawalScreen(tk.Frame):
    def __init__(self, root, user_id, render=False):
        super().__init__(root)
        if render:

            self.user = Users.userwheel[user_id]
            self.user_id = user_id

            self.background_register = PhotoImage(file='image/background_register.png')
            self.button_create = PhotoImage(file='image/button_create.png')
            
            #self.background = tk.Label(root, bd=0, image=self.background_register)
            #self.background.place(width=720, height=1000, x=0, y=0)

            self.saldo = Label(root, text=self.user.balance)
            self.saldo.place(width=205, height=55, x=15, y=127)
            self.saldo.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')

            self.quantia = tk.Entry(root)
            self.quantia.place(width=360, height=42, x=228, y=233)
            self.quantia.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')

            self.saque = tk.Button(root, bd=0, image=self.button_create,command=self.withdrawal)
            self.saque.place(width=445, height=115, x=166, y=710)

            self.back = tk.Button(root, bd=0, image=self.button_create,command=self.sair)
            self.back.place(width=365, height=97, x=176, y=890)
            
    def withdrawal(self):

        if self.user.withdrawal(self.quantia.get()) == True:
            print('foi de certo tudobom')
        else:
            print('algo deu errado na chamada')

    def sair(self):
        if self.user.admin == False:
            app.screen_two(self.user_id)
        elif self.user.admin == True:
            app.screen_three(self.user_id)


class TransferScreen(tk.Frame):
    def __init__(self, root, user_id, render=False):
        super().__init__(root)
        if render:

            self.user = Users.userwheel[user_id]
            self.user_id = user_id

            self.background_register = PhotoImage(file='image/background_register.png')
            self.button_create = PhotoImage(file='image/button_create.png')
            
            #self.background = tk.Label(root, bd=0, image=self.background_register)
            #self.background.place(width=720, height=1000, x=0, y=0)

            self.num = tk.Entry(root)
            self.num.place(width=360, height=42, x=228, y=233)
            self.num.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')

            self.quantia = tk.Entry(root)
            self.quantia.place(width=360, height=42, x=230, y=322)
            self.quantia.config(font='Arieal 20', bd=0,bg= "#0231A0", fg='#ffffff')

            self.saldo = Label(root, text=self.user.balance)
            self.saldo.place(width=205, height=55, x=15, y=127)
            self.saldo.configure(bg='#0231a0', fg='#f7f91f', font='Arieal 20')

            self.tranferir = tk.Button(root, bd=0, image=self.button_create,command=self.transfer)
            self.tranferir.place(width=445, height=115, x=166, y=710)

            self.back = tk.Button(root, bd=0, image=self.button_create,command=self.sair)
            self.back.place(width=365, height=97, x=176, y=890)
            
    def transfer(self):

        if self.user.transfer(self.quantia.get(),self.num.get()) == True:
            print('foi de certo tudobom')
        else:
            print('algo deu errado na chamada')

    def sair(self):
        if self.user.admin == False:
            app.screen_two(self.user_id)
        elif self.user.admin == True:
            app.screen_three(self.user_id)


if __name__ == "__main__":
    app = App()
    Users.create_user('user','12345678910','0',999999999,False,0,'123')
    Users.create_user('adm','10987654321','1',888888888,True,0,'123')
    app.screen_one()
    app.mainloop()