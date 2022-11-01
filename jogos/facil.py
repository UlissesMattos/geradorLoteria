from dataclasses import replace
import random

class Facil:
    volante = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']

    def __init__(self) -> None:
        self

    @classmethod
    def sorteio(cls, quantidade):
        random.shuffle(cls.volante)
        numeros = str(cls.volante[0:quantidade])
        return print(f'Seus números são:', numeros.replace("'", "").replace(',', ' -').replace('[', '').replace(']', ''))