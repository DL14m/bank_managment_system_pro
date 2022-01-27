class Banca:

    __clienti = []
    __conti_correnti = []

    def __init__(self,nome_banca):
        self.__nome_banca = nome_banca


    def __repr__(self):
        return f"Bank:('Name:{self.__nome_banca}, Client:{self.__clienti}, Count:{self.__conti_correnti}')"

    # Getter with methods
    @property
    def nome_banca(self):
        return self.__nome_banca
    # Setter with methods
    @nome_banca.setter
    def nome_banca(self,nome_banca):
        self.__nome_banca = nome_banca


    #Getter
    def get_clienti(self):
        return self.__clienti
    #Setter
    def set_clienti(self,clienti):
        self.__clienti = clienti

    
    def get_conti_correnti(self):
        return self.__conti_correnti
    def set_conti_correnti(self,conti_correnti):
        self.__conti_correnti = conti_correnti