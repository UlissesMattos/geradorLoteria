from dataclasses import replace
import random

class Mega:
    volante = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']

    def __init__(self) -> None:
        self
    
    @classmethod
    def sorteio(cls, quantidade):
        random.shuffle(cls.volante)
        numeros = str(cls.volante[0:quantidade])
        return print(f'Seus números são:', numeros.replace("'", "").replace(',', ' -').replace('[', '').replace(']', ''))

# Mega-Sena
# Recebendo a quantidade de números que deve ser gerada.
#quantidade = int(input('Quantos números você quer gerar? (Escolha de 6 a 15) '))

# O volante contendo os números que podem ser sorteados
#volante = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']

# Sorteando os números
#random.shuffle(volante)

# Recebendo os números sorteados na quantidade desejada
#numeros = str(volante[0:quantidade])

# Mostrando os números gerados ao usuário
#print(f'Seus números são:', numeros.replace("'", "").replace(',', ' -').replace('[', '').replace(']', ''))
