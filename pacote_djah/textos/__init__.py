from pacote_djah.cores import Cores as c

class Titulo:
    '''
    -> Classe para formatação de titulos.
    :param self.msg: Irá receber a mensagem a ser formatada, nas quais você deve escolher o tipo de formatação.
    Created By: Djaaah
    '''
    def __init__(self, msg, cor):
        self.msg = msg
        self.cor = cor    
    def menu_principal(self):
        print('-' * 30)
        print(f'{"Menu Principal":^30}')
        print('-'*30)
        print(self.msg)
        print('-'*30)
    
    def boas_vindas(self):
        tam = len(self.msg) + 15
        print('-'*tam)
        print(f'{self.cor}{self.msg.center(tam)}{c.reset_all}')
        print('-'*tam)
    
    def formatar_titulo(self):
        tam = len(self.msg) + 4
        print('~'*tam)
        print(f'  {self.msg}')
        print('~' * tam)
        
    
def validarEscolha(opcoes, msg, I, F):
    print(f'{opcoes}')
    while True:
        try:
            escolha = int(input(f'{c.fonte_verde}{msg}: {c.reset_all}'))
        except ValueError:
            print(f'{c.fonte_vermelha}Formato incorreto, verifique e tente novamente.{c.reset_all}')
            continue
        if escolha > F or escolha < I:
            print(f'{c.fonte_vermelha}Opção não encontrada.{c.reset_all}')
        else:
            return escolha
            break
        
        
class Validacao:
    def __init__(self, msg, msg_erro, tipo, cor):
        self.msg = msg
        self.tipo = tipo
        self.cor = cor
        self.msg_erro = msg_erro
    
    def validar_tipo(self):
        while True:
            try:
                escolha = self.tipo(input(f'{self.cor}{self.msg}: {c.reset_all}'))
            except ValueError:
                print(f'{c.fonte_vermelha}{self.msg_erro}{c.reset_all}')
                continue
            except Exception as error:
                print(f'{c.fonte_cyan}Erro desconhecido encontrado: {c.reset_all}{c.fonte_vermelha}{error.__class__}{c.reset_all}')
                continue
            else:
                return escolha
                break