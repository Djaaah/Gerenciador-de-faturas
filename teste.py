
from pacote_djah.datas import Datas as d
import sqlite3
bd = sqlite3.Connection('dados.db')
cursor = bd.cursor()

# cursor.execute('SELECT mes_referencia, ano_referencia FROM registros')
# lista = []
# lista_apoio = []
# for i in 
    
# print(lista)

# cursor.execute('SELECT data_compra, descricao_compra, valor_compra, comprador FROM registros WHERE final_cartao = "Final 9674"')
# print(f'{"Data da Compra":<30} {"Descrição da Compra":<30} {"Valor da Compra":<30} {"Comprador":>10}')
# print('-'*140)
# for i in cursor.fetchall():
#     valor = float(i[2])
#     print(f'{i[0] :.<33}{i[1] :.<30}R$ {valor:.<33.2f}{i[3] :<30}')

mes_referencia = d.mesAtual()

print(mes_referencia)