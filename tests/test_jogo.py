from codigo.jogo import Jogo

class TestClass:
    def test_quando_jogo_recebe_tipo_aventura(self):
        entrada='Corrida' # Given
        esperado ='Topgear'

        jogo_teste = Jogo('Teste',entrada,'corrida')
        resultado = jogo_teste.jogo()#When-ação

        assert resultado == esperado #Then-desfecho

        
