
from count import Conto
from bank import Banca
from client import Cliente
from count import ContoSpecial
from persistence import PersistenceHanlder

cliente1 = Cliente('Bobby', 'Firmi', '3924663077')
cliente2 = Cliente('Davide', 'Fella', '3335688985')
cliente3 = Cliente('Marco', 'Casale', '3335688285')
banca_fineco = Banca('Banca San Paolo', 'BA')
banca = Banca('Banca San Gregorio', 'GE')

conto1 = ContoSpecial(1587,cliente1,'12')
conto2 = ContoSpecial(1588,cliente1,'','')
conto3 = ContoSpecial(1685,cliente2,'','')
conto4 = ContoSpecial(1987,cliente3,'','')

banca.add_client(cliente1)
banca.add_client(cliente2)
banca.add_client(cliente3)
banca.open_count(conto1)
banca.open_count(conto2)
banca.open_count(conto3)
banca.open_count(conto4)

""" conto1.pay_money(500)
print('Balance: ' + str(conto1.saldo)) 
print(conto1.take_money(498.5))  """

conto1.pay_money(500)


# Persistenza 
lista_banche = []
lista_banche.append(banca)
lista_banche.append(banca_fineco)

lista_conto = []
lista_conto.append(conto1)
lista_conto.append(conto2)
lista_conto.append(conto3)
lista_conto.append(conto4)

lista_clienti = []
lista_clienti.append(cliente1)
lista_clienti.append(cliente2)
lista_clienti.append(cliente3)


persistenceHanlder = PersistenceHanlder()
persistenceHanlder.bank_save_all(lista_banche)
persistenceHanlder.client_save_all(lista_clienti)
persistenceHanlder.count_save_all(lista_conto)

