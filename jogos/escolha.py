from jogos.mega import Mega
from jogos.facil import Facil

class Escolha:
    def __init__(self) -> None:
        self

    def escolhaJogo():
        while True:
            try:
                jogo = int(input('Qual jogo você quer fazer? (1 - Mega-Sena ou 2 - Lotofácil) '))
            except ValueError:
                print('Digite somente números')
                break
            
            match jogo:
                case 1:
                    while True:
                        try:
                            quantidade = int(input('Quantos números você quer gerar? (Escolha de 6 a 15) '))
                        except ValueError:
                            print('Digite somente números')
                            break

                        if quantidade >= 6 and quantidade <= 15:
                            Mega().sorteio(quantidade)
                            break
                        else:
                            print(f'{quantidade} não é uma opção disponível para esse jogo.')
                    return quantidade
                case 2:
                    while True:
                        try:
                            quantidade = int(input('Quantos números você quer gerar? (Escolha de 15 a 20) '))
                        except:
                            print('Digite somente números')
                            break

                        if quantidade >= 15 and quantidade <= 20:
                            Facil().sorteio(quantidade)
                            break
                        else:
                            print(f'{quantidade} não é uma opção disponível para esse jogo.')
                    return quantidade
                case _:
                    print(f'{jogo} não é uma opção disponível.')
        return jogo        


