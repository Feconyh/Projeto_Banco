
import random

# n tanko documentar saq td n
    #tem o minimo de documentaçãoe
    #porem tae mais so pra n se perder
    #doq pra realmente documentar
# confia q eu entendo
# pode tentra quebrar o codigo ae
# godsorte

# pesoa
#
# classe parente

class pessoa:

    def __init__(self, nome, cpf, nascimento):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento

    def dados(self):
        print("\nNome:", self.nome)
        print("CPF:", self.cpf)
        print("Nascimento:", self.nascimento)


# conta
#
# classe herdada

class conta(pessoa):
    contas = 0

    def __init__(self, nome, cpf, nascimento, numero=0, saldo=0, senha=0,history=[]):
        super().__init__(nome, cpf, nascimento)

        self.numero = numero
        self.saldo = float(saldo)
        self.history = history
        self.history = []
        conta.addconta()
        self.numero = conta.contas
        self.senha = random.randrange(1, 1000)

    def extrato(self):
        print("\nTitular:", self.nome)
        print("Numero:", self.numero)
        print("Senha:", self.senha)
        print("Saldo:", self.saldo)

    def deposito(self, valor):
        self.saldo += valor
        self.history.append("Deposito De {}".format(valor))

    def saque(self, valor):
        self.saldo -= valor
        self.history.append("Saque De {}".format(valor))

    def transferencia(self, quantia, titular):
        self.saldo -= quantia
        cria.lista[titular-1].saldo += quantia
        self.history.append("Transferencia de {} Para a Conta {}".format(quantia,titular))
        cria.lista[titular-1].history.append("Trasferencia de {} por {} ".format(quantia,self.numero))

    def historico(self):
        for contagem in range(len(self.history)):
            print("|- {}".format(self.history[contagem]))

    # add valor +1 pra contagem de total de contas (numero de identificação)
    @classmethod
    def addconta(cls):
        cls.contas += 1


#classe menu
#
#big classe

class cria:

    #contagem big importante
    #armazena todos os objetoss
    lista = []
    contagem = 0

    # menu

    @classmethod
    def menu(cls):
        while True:
            try:
                print("\n------------------------------------------------------------------------------------")
                print("\n 1 - Criar Cadastro")
                print(" 2 - Acessar Conta")
                print(" 3 - Finalizar Programa")

                inpute = input("\n   ==   ")

                if inpute == "1":
                    cria.criacao()
                elif inpute == "2":
                    cria.login()
                elif inpute == "3":
                    print("\n------------------------------------------------------------------------------------")
                    break
                else:
                    print("\n Input Invalido --")
                    continue
            except:
                print("\n Input Invalido --")
                continue

    # criacao

    @classmethod
    def criacao(cls):

        print("\n------------------------------------------------------------------------------------")

        # Nome
        print("\n Nome __")
        name = str(input("\n   ==   "))
        print("\n //////////////////////////////////////////////////////")

        # CPF
        print("\n CPF __")
        while True:
            while True:
                try:
                    cpf = int(input("\n   ==   "))
                    cpf = str(cpf)
                    break
                except:
                    print("\n Somente Numeros--")
                    continue
            if len(cpf) == 11:
                cpf = ("{}.{}.{}-{}".format(cpf[0:3],cpf[3:6],cpf[6:9],cpf[9:11]))
                break
            else:
                print("\n Cpf Invalido --")
        print("\n //////////////////////////////////////////////////////")

        # Nascimento
        print("\n Nascimento __")
        while True:
            try:
                while True:
                    print("\nDia : ")
                    dia = int(input("\n   ==   "))
                    if dia in range(1, 31):
                        break
                    else:
                        print("\n Dia Invalido")
                while True:
                    print("\nMes : ")
                    mes = int(input("\n   ==   "))
                    if mes in range(1, 13):
                        break
                    else:
                        print("\n Mes Invalido")
                print("\nAno : ")
                ano = int(input("\n   ==   "))
                nascimento = ("{}/{}/{}".format(dia, mes, ano))
                break
            except:
                print("\n Sommente Numeros-- \n Repita Tudo --")

                continue

        cria.create(name,cpf,nascimento)
        cria.acesso(cria.contagem-1)

    # login

    @classmethod
    def login(cls):
        while True:
            print("\n------------------------------------------------------------------------------------")
            print("\nNumero de usuario :")
            while True:
                try:
                    numero = int(input("\n   ==   "))
                    break
                except:
                    print("\n Somente Numeros -- ")
                    continue
            print("\n //////////////////////////////////////////////////////")
            print("\nSenha :")
            while True:
                try:
                    senha = int(input("\n   ==   "))
                    break
                except:
                    print("\n Somente Numeros --")
            try:
                if senha == cria.lista[numero-1].senha:
                    cria.acesso(numero-1)
                    break
            except:
                pass
            print("\nSenha/Usuario Incorreto/Inexistente --")
            break

    # acesso

    @classmethod
    def acesso(cls,id):

        print("\n------------------------------------------------------------------------------------")

        while True:
            print("\n 1 - Dados ")
            print(" 2 - Extrato ")
            print(" 3 - Deposito ")
            print(" 4 - Saque ")
            print(" 5 - Transferençia ")
            print(" 6 - Historico ")
            print(" 7 - Deslogar ")
            while True:
                try:
                    inpute = int(input("\n    ==    "))
                    break
                except:
                    print("\n Somente Numeros -- ")
                    continue
            if inpute == 1:
                cria.dado(id)
            elif inpute == 2:
                cria.extrat(id)
            elif inpute == 3:
                cria.deposit(id)
            elif inpute == 4:
                cria.saq(id)
            elif inpute == 5:
                cria.transfe(id)
            elif inpute == 6:
                cria.histor(id)
            elif inpute == 7:
                break
            else:
                print("\n Numero Invalido --")
                continue

    # dados

    @classmethod
    def dado(cls,id):
                print("\n //////////////////////////////////////////////////////")
                cria.lista[id].dados()
                print("\n //////////////////////////////////////////////////////")

    # extrato

    @classmethod
    def extrat(cls,id):
                print("\n//////////////////////////////////////////////////////")
                cria.lista[id].extrato()
                print("\n //////////////////////////////////////////////////////")

    # deposito

    @classmethod
    def deposit(cls,id):
            print("\n //////////////////////////////////////////////////////")
            while True:
                try:
                    print("\n Quantia : ")
                    quantia = float(input("\n    ==    "))
                    if quantia <= 0:
                        print("\n Input Invalido --")
                        continue
                    else:
                        cria.lista[id].deposito(quantia)
                        print("\n //////////////////////////////////////////////////////")
                        break
                except:
                    print("\n //////////////////////////////////////////////////////")
                    print("\n Input Invalido --\n Tente a Operação Novamente --")
                    print("\n //////////////////////////////////////////////////////")
                    break

    # saque

    @classmethod
    def saq(cls,id):
        print("\n //////////////////////////////////////////////////////")
        if cria.lista[id].saldo > 0:
            while True:
                try:
                    print("\n Quantia : ")
                    quantia = float(input("\n    ==    "))
                    if quantia <= 0:
                        print("\n Input Invalido --")
                        continue
                    else:
                        if cria.lista[id].saldo >= quantia:
                            cria.lista[id].saque(quantia)
                            print("\n //////////////////////////////////////////////////////")
                            break
                        else:
                            print("\n Saldo Insuficiente --")

                except:
                    print("\n //////////////////////////////////////////////////////")
                    print("\n Input Invalido --\n Tente a Operação Novamente --")
                    print("\n //////////////////////////////////////////////////////")
                    break
        else:
            print("\n Saldo Insuficiente --")
            print("\n //////////////////////////////////////////////////////")

    # transferencias

    @classmethod
    def transfe(cls,id):
            if cria.lista[id].saldo > 0:
                print("\n //////////////////////////////////////////////////////")
                print("\n Quantia")
                while True:
                    try:
                        quantia = float(input("\n    ==    "))
                        if quantia >= 1 and quantia <= cria.lista[id].saldo:
                            break
                        else:
                            print("\n Input Invalido -- ")
                            continue
                    except:
                        print("\n Input Invalido --")
                        continue
                print("\n //////////////////////////////////////////////////////")
                print("\n Numero Do Titular")
                while True:
                    try:
                        titular = int(input("\n    ==    "))
                        if titular <= 0 or titular == cria.lista[id].numero:
                            print("\n Input Invalido --")
                            continue
                        else:
                            break
                    except:
                        print("\n Input Invalido --")
                        continue
                try:
                    cria.lista[id].transferencia(quantia,titular)
                except:
                    print("\n Conta Inexistente --")
                    print("\n //////////////////////////////////////////////////////")
            else:
                print("\n //////////////////////////////////////////////////////")
                print("\n Saldo Insuficiente --")
                print("\n //////////////////////////////////////////////////////")

    # historico

    @classmethod
    def histor(cls,id):
            print("\n------------------------------------------------------------------------------------")
            print("\n Historico :")
            print("\n //////////////////////////////////////////////////////")
            cria.lista[id].historico()
            print("\n //////////////////////////////////////////////////////")


    # criacao ++ de conta

    @classmethod
    def create(cls, nombre, cpf, idade):

        global contagem
        global lista

        cria.contagem += 1
        cria.lista.append(cria.contagem)
        cria.lista[cria.contagem - 1] = conta(nombre, cpf, idade)

        #mostralista
        #print("\n Lista : {} \n contagem : {}".format(cria.lista, cria.contagem))


# Run Zone
#
# Cria umas conta admin ae e roda o menu

cria.create("admin1","123.456.789-10","10/10/10")
cria.lista[0].senha = 1
cria.create("admin2","10.987.654.321","01/01/01")
cria.lista[1].senha = 2
cria.menu