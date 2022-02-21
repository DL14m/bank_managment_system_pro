
from count import Conto

class Cliente:

    def __init__(self,nome_cliente,cognome_cliente,numero_telefono ):
        self.__nome_cliente = nome_cliente
        self.__cognome_cliente = cognome_cliente
        self.__numero_telefono = numero_telefono
        self.__id = id(self)
        print(f'Bank instance created with ID: {self.__id}')


    @property
    def id(self): 
        return self.__id
    @id.setter
    def id(self, id): 
        self.__id = id

    # Getter with methods
    @property
    def nome_cliente(self):
        return self.__nome_cliente
    # Setter with methods
    @nome_cliente.setter
    def nome_cliente(self,nome_cliente):
        self.__nome_cliente = nome_cliente


    @property
    def numero_telefono(self):
        return self.__numero_telefono
    @numero_telefono.setter
    def numero_telefono(self,numero_telefono):
        self.__numero_telefono = numero_telefono
    

    @property
    def cognome_cliente(self):
        return self.__cognome_cliente
    # Setter with methods
    @cognome_cliente.setter
    def cognome_cliente(self,cognome_cliente):
        self.__cognome_cliente = cognome_cliente

    
    def print_surname_balance(self):
        return f'Surname:{self.__id}, Balance:{Conto.saldo}'

    
    def print_surname_codecount(self):
        return f'Surname:{self.__id}, Code Count:{Conto.numero_conto}'


    def __repr__(self):
        return f"Client:('ID:{self.__id}, Name:{self.__nome_cliente}, Surname:{self.__cognome_cliente}, Phone:{self.__numero_telefono}')"
