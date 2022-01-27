from itertools import count
from count import Conto
from bank import Banca
from client import Cliente

cliente1 = Cliente('Bob', '3924663077')
cliente2 = Cliente('Davide', '3335688985')
cliente3 = Cliente('Marco', '3335688285')
banca = Banca('Banca San Paolo')
account = Conto('00001',cliente1,'12','12')

print(account)
print(banca)
print(cliente1)
