class Conto:

    __operazioni_effettuate = []

    def __init__(self,numero_conto,cliente,bilancio_conto,saldo=0):
        self.__numero_conto = numero_conto
        self.__cliente = cliente
        self.__bilancio_conto = bilancio_conto
        self.__saldo = saldo


    def __repr__(self):
        return f"Count:('Number of Count:{self.__numero_conto}, {self.__cliente}, Operation:{self.__operazioni_effettuate}, Balance:{self.__saldo}, Account Budget:{self.__bilancio_conto}')"


    # Getter
    def get_numero_conto(self):
        return self.__numero_conto
    # Setter 
    def set_numero_conto(self,numero_conto):
        self.__numero_conto = numero_conto


    # Getter with methods
    @property
    def cliente(self):
        return self.__cliente
    # Setter with methods
    @cliente.setter
    def cliente(self,cliente):
        self.__cliente = cliente


    def get_operazioni_effettuate(self):
        return self.__operazioni_effettuate
    def set_operazioni_effettuate(self,operazioni_effettuate):
        self.__operazioni_effettuate = operazioni_effettuate

    
    def get___bilancio_conto(self):
        return self.__bilancio_conto
    def set___bilancio_conto(self,bilancio_conto):
        self.__bilancio_conto = bilancio_conto

    
    def get_saldo(self):
        return self.__saldo
    def set_numero_conto(self,saldo):
        self.__saldo = saldo
