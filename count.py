
from logging import exception

class Conto:

    __operazioni_effettuate = []

    def __init__(self,numero_conto,cliente,bilancio_conto,saldo=0):
        self.__numero_conto = numero_conto
        self.__cliente = cliente
        self.__bilancio_conto = bilancio_conto
        self.__saldo = saldo
        self.__id = id(self)
        print(f'Bank instance created with ID: {self.__id}')


    @property
    def id(self): 
        return self.__id


    # Getter with methods
    @property
    def numero_conto(self):
        return self.__numero_conto
    # Setter with methods
    @numero_conto.setter 
    def numero_conto(self,numero_conto):
        self.__numero_conto = numero_conto


    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self,cliente):
        self.__cliente = cliente


    @property
    def operazioni_effettuate(self):
        return self.__operazioni_effettuate
    @operazioni_effettuate.setter
    def operazioni_effettuate(self,operazioni_effettuate):
        self.__operazioni_effettuate = operazioni_effettuate

    
    @property
    def bilancio_conto(self):
        return self.__bilancio_conto
    @bilancio_conto.setter
    def bilancio_conto(self,bilancio_conto):
        self.__bilancio_conto = bilancio_conto

    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    
    def __repr__(self):
        return f"Count:('Number of Count:{self.__numero_conto}, {self.__cliente}, Operation:{self.__operazioni_effettuate}, Balance:{self.__saldo}, Account Budget:{self.__bilancio_conto}')"


    def pay_money(self, value): 
        value = int(input ('Enter how much money you want to deposit to increase the balance'))
        self.__saldo += value
        print(f'Payment was successful and the balance is {self.__saldo}€')


    def take_money (self, value):
        value = int(input ('Enter how much money you want to withdraw by decreasing the balance'))
        if value < self.__saldo:
            self.__saldo -= value
            print(f'Withdrawal was successful and the balance is {self.__saldo}€')
        else:
            print(f'Error, the balance is too low for withdraw that cipher, the balance is {self.__saldo}€')
