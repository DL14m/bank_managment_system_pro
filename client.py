
class Cliente:

    def __init__(self,nome_cliente,numero_telefono ):
        self.__nome_cliente = nome_cliente
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
    
    
    def __repr__(self):
        return f"Client:('ID:{self.__id}, Name:{self.__nome_cliente}, Phone:{self.__numero_telefono}')"
