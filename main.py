
from count import Conto
from bank import Banca
from client import Cliente

cliente1 = Cliente(0,'Bob', '3924663077')
cliente2 = Cliente(1,'Davide', '3335688985')
cliente3 = Cliente(2,'Marco', '3335688285')
banca = Banca('Banca San Paolo')

conto1 = Conto(1587,cliente1,'12')
conto2 = Conto(1588,cliente1,'','')
conto3 = Conto(1685,cliente2,'','')
conto4 = Conto(1987,cliente3,'','')

banca.add_client(cliente1)
banca.add_client(cliente2)
banca.add_client(cliente3)
banca.open_count(conto1)
banca.open_count(conto2)
banca.open_count(conto3)
banca.open_count(conto4)

 