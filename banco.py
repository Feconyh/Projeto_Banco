from tkinter import *
import HelpPlace

root = Tk()
root.title('Cadastro')
root.geometry('600x900+300+300')
root.iconbitmap(default="Projeto_Banco\image\player.ico")
root.resizable(width=False, height=False)

root.bind('<Button-1>', HelpPlace.inicio_place)
root.bind('<ButtonRelease-1>', lambda arg: HelpPlace.fim_place(arg, root))
root.bind('<Button-2>', lambda arg: HelpPlace.para_geometry(root))

class Layout:
    pass

class Command:
    
    @staticmethod
    def clear():
        for widget in root.winfo_children():
            widget.destroy()
    
    def confirm_deposit():
        pass
    
    def confirm_withdraw():
        pass

class Screen():

    @staticmethod
    def login(self):

        self.frame = Frame(root, bg='blue')
        self.frame.place(side = LEFT)

        self.login_lb = Label(self.frame,text='Login',bg='blue', fg='orange')
        self.login_lb.place(width=83, height=28, x=29, y=36)
        
        self.user_lb = Label(self.frame,text='Login',bg='blue', fg='white')
        self.user_lb.place(width=83, height=28, x=29, y=36)
        
        self.password_lb = Label(self.frame,text='Login',bg='blue', fg='white')
        self.password_lb.place(width=83, height=28, x=29, y=36)


        self.user_ent = Entry(self.frame,text='Login')
        self.user_ent.place(width=83, height=28, x=29, y=36)

        self.password_ent = Entry(self.frame,text='Login')
        self.password_ent.place(width=83, height=28, x=29, y=36)
        
        self.login_btn = Button(self.frame,text='Login',bg='orange', fg='white')
        self.login_btn.place(width=83, height=28, x=29, y=36)

    @staticmethod
    def user():
        # Limpa e cria o layout primeira tela
        Command.clear()
        '''
        Layout da tela
        '''  

    @staticmethod
    def extract():
        # Limpa e cria o layout primeira tela
        Command.clear()
        '''
        Layout da tela
        '''    

    @staticmethod
    def deposit():
        # Limpa e cria o layout primeira tela
        Command.clear()
        '''
        Layout da tela
        '''      
    
    @staticmethod
    def cash_withdrawal():
        # Limpa e cria o layout primeira tela
        Command.clear()
        '''
        Layout da tela
        ''' 

    @staticmethod
    def perfil():
        # Limpa e cria o layout primeira tela
        Command.clear()
        '''
        Layout da tela
        '''

root.mainloop()