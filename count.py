class Conto:

    operazioni_effettuate = []

    def __init__(self,numero_conto,cliente,bilancio_conto,saldo=0):
        self.numero_conto = numero_conto
        self.cliente = cliente
        self.bilancio_conto = bilancio_conto
        self.saldo = saldo

    def __repr__(self):
        return f"Count:('Number of Count:{self.numero_conto}, {self.cliente}, Operation:{self.operazioni_effettuate}, Balance:{self.saldo}, Account Budget:{self.bilancio_conto}')"
