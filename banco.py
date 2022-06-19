import tkinter as tk
from tkinter import *
import HelpPlace

class Command:
    
    @staticmethod
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def confirm_deposit():
        pass
    
    def confirm_withdraw():
        pass

class Screen():

    @staticmethod
    def login(self):
        self.configure(bg='#0231a0')

        self.tumb_log = tk.Label(self, image=self.tumb_one)
        self.tumb_log.place(width=360, height=1000, x=360, y=0)

        self.login_log = tk.Label(self, image=self.login)
        self.login_log.place(width=175, height=69, x=30, y=36)

        self.user_log = tk.Label(self, image=self.user)
        self.user_log.place(width=180, height=50, x=30, y=260)

        self.password_log = tk.Label(self, image=self.password)
        self.password_log.place(width=140, height=50, x=30, y=400)
        

        self.user_ent = tk.Entry(self,text='Login')
        self.user_ent.place(width=180, height=20, x=30, y=320)

        self.password_ent = tk.Entry(self,text='Login')
        self.password_ent.place(width=180, height=20, x=30, y=460)

        self.login_btn = tk.Button(self, bd=0, image=self.button_login, command=Command.clear)
        self.login_btn.place(width=300, height=118, x=30, y=520)
   
    @staticmethod
    def adm(self):
        self.configure(bg='#ec7001')
    
        self.header_user = tk.Label(self, bd=0, image=self.header)
        self.header_user.place(width=720, height=200, x=0, y=0)

        self.historic_user = tk.Button(self, bd=0, image=self.historic)
        self.historic_user.place(width=720, height=100, x=0, y=200)


        self.extract_btn = tk.Button(self, bd=0, image=self.extract)
        self.extract_btn.place(width=225, height=140, x=50, y=340)

        self.deposit_btn = tk.Button(self, bd=0, image=self.deposit)
        self.deposit_btn.place(width=225, height=140, x=410, y=340)
        
        self.withdrawal_btn = tk.Button(self, bd=0, image=self.withdrawal)
        self.withdrawal_btn.place(width=225, height=140, x=50, y=520)
        
        self.transfer_btn = tk.Button(self, bd=0, image=self.transfer)
        self.transfer_btn.place(width=225, height=140, x=410, y=520)
        
        self.exit_btn = tk.Button(self, bd=0, image=self.exit)
        self.exit_btn.place(width=225, height=140, x=50, y=700)

        self.cuie_user = tk.Label(self, bd=0, image=self.cuie)
        self.cuie_user.place(width=225, height=200, x=410, y=700)

        self.bottom_bar_user = tk.Label(self, bd=0, image=self.bottom_bar)
        self.bottom_bar_user.place(width=720, height=100, x=0, y=900)

    def user(self):
        self.configure(bg='#ec7001')
    
        self.header_user = tk.Label(self, bd=0, image=self.header)
        self.header_user.place(width=720, height=200, x=0, y=0)

        self.historic_user = tk.Button(self, bd=0, image=self.historic)
        self.historic_user.place(width=720, height=100, x=0, y=200)


        self.extract_btn = tk.Button(self, bd=0, image=self.extract)
        self.extract_btn.place(width=225, height=140, x=50, y=340)

        self.deposit_btn = tk.Button(self, bd=0, image=self.deposit)
        self.deposit_btn.place(width=225, height=140, x=410, y=340)
        
        self.withdrawal_btn = tk.Button(self, bd=0, image=self.withdrawal)
        self.withdrawal_btn.place(width=225, height=140, x=50, y=520)
        
        self.transfer_btn = tk.Button(self, bd=0, image=self.transfer)
        self.transfer_btn.place(width=225, height=140, x=410, y=520)
        
        self.exit_btn = tk.Button(self, bd=0, image=self.exit)
        self.exit_btn.place(width=225, height=140, x=50, y=700)

        self.cuie_user = tk.Label(self, bd=0, image=self.cuie)
        self.cuie_user.place(width=225, height=200, x=410, y=700)

        self.bottom_bar_user = tk.Label(self, bd=0, image=self.bottom_bar)
        self.bottom_bar_user.place(width=720, height=100, x=0, y=900)

    @staticmethod
    def extract():
        '''
        Layout da tela
        '''    

    @staticmethod
    def deposit():
        '''
        Layout da tela
        '''      
    
    @staticmethod
    def cash_withdrawal():
        '''
        Layout da tela
        ''' 

    @staticmethod
    def perfil():
        '''
        Layout da tela
        '''

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Cadastro')
        self.geometry("720x1000+610+0")
        self.iconbitmap(default="image\player.ico")
        self.resizable(width=False, height=False)

        self.bind('<Button-1>', HelpPlace.inicio_place)
        self.bind('<ButtonRelease-1>', lambda arg: HelpPlace.fim_place(arg, self))
        self.bind('<Button-2>', lambda arg: HelpPlace.para_geometry(self))

        # importação de imagem da tela de login
        self.tumb_one = PhotoImage(file="image/Tumb.png")
        self.entry = PhotoImage(file='image/entry.png')
        self.login = PhotoImage(file='image/login.png')
        self.user = PhotoImage(file='image/usuario.png')
        self.password = PhotoImage(file='image/senha.png')
        self.button_login = PhotoImage(file='image/button_login.png')

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

if __name__ == "__main__":

    app = App()

    Screen.adm(app)

    app.mainloop()