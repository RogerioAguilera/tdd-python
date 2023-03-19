from codigo.loja import Empresa

class TestClass:
    def test_quando_tempo_empresa_15_02_1999_deve_retornar_24(self):
        entrada='15/02/1999' # Given
        esperado = 24

        empresa_teste = Empresa('Teste',entrada,1112)
        resultado= empresa_teste.tempo_empresa() # When

        assert resultado == esperado # Then

    def test_quando_razao_social_recebe_Torino_Camisetas_deve_retornar_Torino_ME(self):
        entrada = 'Torino Camisetas'   # Given
        esperado = 'Torino ME'

        torino = Empresa(entrada,'11/12/1999', 1112)
        resultado = torino.razao_social() # When

        assert resultado == esperado

    def test_quando_decrescimo_faturamento_diario_recebe_100000_deve_retornar_90000(self):
        entrada_faturamento_diario= 100000 # given
        entrada_nome_fantasia= 'Faraday Eletrônica'
        esperado = 90000

        empresa_teste= Empresa(entrada_nome_fantasia,'11/12/1999', entrada_faturamento_diario)
        empresa_teste.decrescimo_faturamento_diario() # when
        resultado = empresa_teste.faturamento_diario

        assert resultado == esperado # then


        
