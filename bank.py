class Banca:

    clienti = []
    conti_correnti = []

    def __init__(self,nome_banca):
        self.nome_banca = nome_banca

    def __repr__(self):
        return f"Bank:('Name:{self.nome_banca}, Client:{self.clienti}, Count:{self.conti_correnti}')"