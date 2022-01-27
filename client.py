class Cliente:

    def __init__(self,nome_cliente,numero_telefono ):
        self.__nome_cliente = nome_cliente
        self.__numero_telefono = numero_telefono


    def __repr__(self):
        return f"Client:('Name:{self.__nome_cliente}, Phone:{self.__numero_telefono}')"

    # Getter with methods
    @property
    def nome_cliente(self):
        return self.__nome_cliente
    # Setter with methods
    @nome_cliente.setter
    def nome_cliente(self,nome_cliente):
        self.__nome_cliente = nome_cliente

    # Getter
    def get_numero_telefono(self):
        return self.__numero_telefono
    #Setter
    def set_clienti(self,numero_telefono):
        self.__numero_telefono = numero_telefono
