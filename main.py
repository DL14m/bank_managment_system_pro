
from count import Conto
from bank import Banca
from client import Cliente
from count import ContoSpecial

cliente1 = Cliente('Bob', '3924663077')
cliente2 = Cliente('Davide', '3335688985')
cliente3 = Cliente('Marco', '3335688285')
#banca_fineco = Banca('Banca San Paolo')
banca = Banca('Banca San Paolo', 'GE')

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

conto1.pay_money(500)
print('Balance: ' + str(conto1.saldo)) 
print(conto1.take_money(498.5)) 
 