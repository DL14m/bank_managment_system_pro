
from client import Cliente
from utility import Utility

class Banca:

    def __init__(self, nome_banca, nazione = 'IT'):
        self.__nome_banca = nome_banca
        self.__clienti = []
        self.__conti_correnti = []
        self.__nazione = nazione
        self.__id = id(self)
        print(f'Bank instance created with ID: {self.__id}')


    # Getter with methods
    @property
    def nome_banca(self):
        return self.__nome_banca
    # Setter with methods
    @nome_banca.setter
    def nome_banca(self,nome_banca):
        self.__nome_banca = nome_banca
    

    @property
    def id(self): 
        return self.__id


    @property
    def clienti(self):
        return self.__clienti
    @clienti.setter
    def clienti(self,clienti):
        self.__clienti = clienti


    @property
    def conti_correnti(self):
        return self.__conti_correnti
    @conti_correnti.setter
    def conti_correnti(self,conti_correnti):
        self.__conti_correnti = conti_correnti

    
    @property
    def nazione(self):
        return self.__nazione
    @nazione.setter
    def nazione(self,nazione):
        self.__nazione = nazione



    def __repr__(self):
        return f"Bank:('Name:{self.__nome_banca}, Nation: {self.__nazione}, Client {str(len(self.clienti))}, Count: {str(len(self.conti_correnti))}"
    
    
    def open_count(self, conto):
        self.conti_correnti.append(conto)

    def close_count(self, numero_conto):
        assert Utility.is_integer(numero_conto), "Insert integer number: "        
        assert int(numero_conto) > 0, "Insert valid value"

        pos=-1
        for index in range(0, len(self.conti_correnti)): 
            if self.conti_correnti[index].numero_conto == int(numero_conto):
                pos = index
                break
        
        if pos<0: 
            print("ERROR: Count Number not found")
        else: 
            self.conti_correnti.pop(pos)
            print("Count" + str(numero_conto) + " successfully removed")


    def add_client(self, cliente):
        self.clienti.append(cliente)

    def remove_client(self, id):
        assert Utility.is_integer(id), "Insert ID number: "        
        assert int(id) > 0, "Insert valid value"

        pos=-1
        for index in range(0, len(self.clienti)): 
            if self.clienti[index].id == int(id):
                pos = index
                break
        
        if pos<0: 
            print("ERROR: Client ID not found")
        else: 
            self.clienti.pop(pos)
            print("Count" + str(id) + " successfully removed")

