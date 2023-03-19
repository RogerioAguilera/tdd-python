
from datetime import date

class Empresa:

    def __init__(self,nome_fantasia,data_abertura_loja,faturamento_diario):
        self._nome_fantasia = nome_fantasia
        self._data_abertura_loja = data_abertura_loja
        self._faturamento_diario = faturamento_diario

    @property
    def nome_fantasia(self):
        return self.nome_fantasia
    
    @property
    def faturamento_diario(self):
        return self.faturamento_diario
    
    def tempo_empresa(self):
        data_abertura_loja = self.data_abertura_loja
        ano_abertura= data_abertura_loja[-1]
        ano_atual=date.today().year
        return ano_atual -int(ano_abertura)
    
    def razao_social(self):
        nome_razaosocial=self.nome.strip()
        nome_quebrado =nome_razaosocial.split(' ')
        return nome_quebrado[-1]
    
    def _eh_socio(self):
        razoes_sociais=['Pitanga Alimentos ME', 'Dont Save EPP','MK Jogos e CIA ME', 'Savana Hotel EPP']
        return (self._faturamento_diario >= 200000) and (self.razao_social() in razoes_sociais)
    
    def decrescimo_faturamento_diario(self):
        if self._eh_socio():
            decrescimo=self.faturamento_diario * 0.1
            self._faturamento_diario=self._faturamento_diario - decrescimo

    def clacular_bonus(self):
        valor = self._faturamento_diario * 0.1
        if valor > 250000:
            valor = 0
        return valor
    
    def __str__(self):
        return f'Empresa({self._nome_fantasia}, {self._data_abertura_loja}, {self._faturamento_diario}, {self._faturamento_diario})'
    
    

    
