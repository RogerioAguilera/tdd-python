from codigo.loja import Empresa

def teste_data_abertura_loja():
    empresa_teste = Empresa('Teste','13/12/1999', 1112)
    print(f'Teste = {empresa_teste._data_abertura_loja()}')

    empresa_teste1 = Empresa('Teste','13/12/1998','1112')
    print(f'Teste = {empresa_teste1._data_abertura_loja()}')

    empresa_teste2 = Empresa('Teste','02/12/1998',1112)
    print(f'Teste = {empresa_teste2._data_abertura_loja()}')

teste_data_abertura_loja()

