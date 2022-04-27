def fatorial(n=1):
    '''
    - > Função desenvolvida para resolução de Fatoriais.
    param n: Número que deseja saber o fatorial.
    return: valor final.
    Created By: Djaaah
    '''
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f

def tirarMedia(*n):
    """
    - > Função para retornar a média simples com a quantidade que julgar necessária de valores.
    param n: valores, pode botar quantas desejar, inteiros ou flutuantes.
    return: media, soma de todas os valores e divisão pela quantidade de valores inseridas.
    Created By: Djaaah
    """
    media = sum(n) / len(n)
    return media

def tornarMoeda(n=0, m='R$'):
    return f'{m} {n:.2f}'.replace('.', ',')


class Conversor:
    def __init__(self, und1, und2, valor, convertido = 0):
        self.und1 = und1
        self.und2 = und2
        self.valor = valor
        self.convertido = convertido
        self.unidades = ['Quilômetro' ,'Hectômetro' ,'Decâmetro', 'Metro', 'Decímetro', 'Centímetro', 'Milímetro']


    def conversao(self):
        distancia = self.und1 - self.und2
        if distancia < 0:
            distancia *= -1
            base = 0
            valor_base = 1
            while base < distancia:
                valor_base *= 10
                base += 1
            self.convertido = (self.valor * valor_base)
            return self.convertido
        else:
            base = 0
            valor_base = 1
            while base < distancia:
                valor_base *= 10
                base += 1
            self.convertido = (self.valor / valor_base)
            return self.convertido       
        
        
class Exchange:
    import requests as r
    from pacote_djah.textos import validarEscolha as v
    import os
    from pacote_djah.cores import Cores as c
    req = r.get('https://api.exchangerate-api.com/v6/latest')
    dados = req.json()
    n = 1 
    print(f'Ultima atualização: {dados["time_last_update_utc"][6:16]}')
    for i in dados['rates'].keys():
        print(f'{n} - {i}')
        n += 1
    n = 1
    escolha = v('Digite a primeira moeda', 1, 161)
    escolha -= 1 
    moedas = list(dados['rates'].items())
    moeda1 = moedas[escolha][0]
    valor_moeda1 = moedas[escolha][1]
    os.system('cls')
    print(f'Certo você escolheu {moeda1} como sua primeira moeda.')
    for i in dados['rates'].keys():
        print(f'{n} - {i}')
        n += 1
    escolha2 = v('Digite a segunda moeda', 1, 161)
    escolha2 -= 1
    moeda2 = moedas[escolha2][0]
    valor_moeda2 = moedas[escolha2][1]
    print(f'Certo anotei aqui que a primeira moeda é: {moeda1} e a segunda é: {moeda2}.')
    while True:
        try:
            valor_possuido = float(input(f'Digite a quantidade de {moeda1} que você possui: $ '))
        except ValueError:
            print(f'{c.fonte_vermelhoClaro}Dado inserido incorretamente. Tente novamente{c.reset_all}')
            continue
        else:
            break
    if valor_moeda1 > valor_moeda2:
        valor_apoio1 = valor_moeda1 / valor_moeda2
        
    else:
        valor_apoio1 = valor_moeda2 / valor_moeda1
        
    
    
    print(f'{c.fonte_cyan}Resultado da conversão{c.reset_all}')
    print(f'{c.fonte_verde}{moeda1}: {valor_possuido:.2f}{c.reset_all}')
    print(f'{c.fonte_amarela}{moeda2}: {valor_apoio1:.2f}{c.reset_all}')
    # def __init__(self, moeda1, moeda2):
    #     self.moeda1 = moeda1
    #     self.moeda2 = moeda2
    