class Cliente:

    def __init__(self,nome_cliente,numero_telefono ):
        self.nome_cliente = nome_cliente
        self.numero_telefono = numero_telefono

    def __repr__(self):
        return f"Client:('Name:{self.nome_cliente}, Phone:{self.numero_telefono}')"
