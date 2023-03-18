
class Jogo:

    def __init__(self,nome):
        self.nome = nome

    def __str__(self):
        return self.nome
    
nbajam= Jogo('Nbajam')
print(nbajam)

topgear = Jogo('Topgear')
print(topgear)

class TipoJogo:
      def __init__(self,tipo):
           self.tipo = tipo
      def __str__(self):
           return self.tipo

ação= TipoJogo('Ação')
print(ação)

aventura= TipoJogo('Aventura')
print(aventura)

estratégia= TipoJogo('Estratégia')
print(estratégia)

corrida= TipoJogo('Corrida')
print(corrida)

esporte= TipoJogo('Esporte')
print(esporte)
