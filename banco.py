from tkinter import *
import HelpPlace

root = Tk()
root.title('Cadastro')
root.geometry('1280x720+300+300')
root.iconbitmap(default="image/player.ico")
root.resizable(width=False, height=False)

root.bind('<Button-1>', HelpPlace.inicio_place)
root.bind('<ButtonRelease-1>', lambda arg: HelpPlace.fim_place(arg, root))
root.bind('<Button-2>', lambda arg: HelpPlace.para_geometry(root))

class Layout:
    def __init__(self):
        super().__init__()
        # função titulo,| nome da var, texto da var, cordenadas y, x |
        @staticmethod
        def title(var, frame,text,width,height,x,y):
            var = Label(frame, bg='gray', text=text)
            var.place(width=width, height=height, x=x, y=y)

        # função caption,| nome da var, texto da var, cordenadas y, x |
        @staticmethod
        def caption(var, frame,text,width,height,x,y):
            var = Label(frame, bg='gray', text=text)
            var.place(width=width, height=height, x=x, y=y)

        @staticmethod
        def entry(var, frame,width,height,x,y, show=''):
            var = Entry(frame, show=show)
            var.place(width=width, height=height, x=x, y=y)

        @staticmethod
        def button(var, frame,text,command,width,height,x,y):
            var = Button(frame, text=text, command=command)
            var.place(width=width, height=height, x=x, y=y)

        @staticmethod
        def chckbttn(var, frame,text,width,height,x,y):
            var = Checkbutton(frame, bg='gray', text=text, width=15)
            var.place(width=width, height=height, x=x, y=y)

class Command:

    @staticmethod
    def clear():
        for widget in root.winfo_children():
            widget.destroy()
    
    def confirm_deposit():
        pass
    
    def confirm_withdraw():
        pass

class Screen:

    @staticmethod
    def login():
        # Limpa e cria o layout primeira tela
        Command.clear()

        frame = Frame(root, bg='gray', borderwidth=2, relief='groove')

        '''
        Layout da tela
        '''

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