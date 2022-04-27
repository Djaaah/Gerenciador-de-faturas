import sqlite3
import PySimpleGUI as sg
from pacote_djah.datas import Datas as d

bd = sqlite3.Connection('dados.db')
cursor = bd.cursor()


class Telas:
    def tela_principal():
        sg.theme('GreenMono')
        cursor.execute('SELECT * FROM cartoes')
        layout = [
            [sg.Combo(Funcoes.GET_CARTOES(), readonly=True, default_value='SELECIONAR CARTÃO', key='-Cartao_Selecionado-', size=(24,0))],
            [sg.Button('Adicionar Registro', key='-Adc_Registro-', border_width=0, size=(22,0))],
            [sg.Button('Adicionar Cartão', key='-Novo_Cartao-', border_width=0, size=(22,0))],
            [sg.Button('Ver Faturas', key='-Ver_Fatura-', border_width=0, size=(22,0))],
            [sg.Button('Filtros', key='-Filtros-', border_width=0, size=(22,0))]
        ]
        return sg.Window('Menu Principal', layout=layout, finalize=True)
    
    
    def ver_fatura(valor):
        sg.theme('GreenMono')
        
        layout = [
            [sg.Input(f"{valor['-Cartao_Selecionado-']}", key='-Cartao_Selecionado-', disabled=True, border_width=0, )],
            [sg.Combo(Funcoes.SELECIONAR_FATURA(valor), readonly=True, default_value='SELECIONAR FATURA', size=(24,0), key='-Fatura_Selecionada-')],
            [sg.Button('Confirmar', key='-Confirmar-', border_width=0), sg.Button('Cancelar', border_width=0, key='-Cancelar-')]
        ]
        return sg.Window('Selecionar Fatura', layout=layout, finalize=True)
    
    
    def ver_fatura_selecionada(valor):
        sg.theme('GreenMono')  
        
        lista_compradores, compradores_cabecalho = Funcoes.LISTA_COMPRADORES(valor)
        cabecalho = Funcoes.DADOS_FATURA_SELECIONADA(valor)[0]
        dados = Funcoes.DADOS_FATURA_SELECIONADA(valor)[1]
        cartao = valor['-Cartao_Selecionado-']
        vencimento, valor_total = Funcoes.VENCIMENTO_VALOR_TOTAL(valor)
        
        compradores_tabela = [
            [sg.Table(values=lista_compradores, headings=compradores_cabecalho,
                      auto_size_columns=True, 
                      justification='center',
                      num_rows=4, 
                )]
        ]

        layout = [
            [sg.Text(f'Cartão: {cartao}\nVencimento: {vencimento}\nValor Total R$ {valor_total:.2f}'), sg.Column(compradores_tabela)],
            [sg.Table(values=dados, headings=cabecalho,
                      auto_size_columns=True, 
                      justification='center',
                      num_rows=10,
                )],
            [sg.Button('Voltar', key='-Voltar-', border_width=0), sg.Button('Gerar Relatório', key='-Gerar_Relatório-', border_width=0)]
        ]

        return sg.Window('Fatura Selecionada', layout=layout, finalize=True)
    
    def adc_cartao():
        sg.theme('GreenMono')
        dia = []
        for i in range(1, 32):
            dia.append(i)
        layout = [
            [sg.Text('Final do Cartão', size=(15,0)), sg.Input(key='-Adicionar_Cartao-', border_width=0, do_not_clear=False)],
            [sg.Text('Vencimento do Cartão', size=(15,0)), sg.Combo(dia, readonly=True, key='-Vencimento-')],
            [sg.Button('Incluir Cartão', border_width=0, key='-Incluir_Cartao-', size=(10,1)), sg.Button('Cancelar', border_width=0, key='-Cancelar-')]
        ]
        return sg.Window('Adicionar Cartões', layout=layout, finalize=True)
    
    
    def adc_registro(valor):
        sg.theme('GreenMono')
        dia = []
        for i in range(1, 32):
            dia.append(i)
        vezes = []
        for i in range(2, 25):
            vezes.append(i)
        ano = []
        for i in range(2021, 2030):
            ano.append(i)
        global mes
        mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        
        btn_pesq = 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAAsQAAALEBxi1JjQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAEeSURBVEiJ7dQ5TkMxEMbxXx5HYOmDBBwAjpJNuRBLkx5yiSQ9BwABF2CpAGWBHppHYSNQRIKdKA3ia97ikf8zn2fMv5ZQgTYGeMJbfPbRiusLaxvXKHGLUxzhDHfx/xWqi24+whg1VKbWK6hjgmEupIiZj7HzS+xuhFzKsKstlF9LjG/G+GYqYCB4Pm3LLFVwj96sgOnS9nEes0pRGeMPUgHrgq85GmEjFfCCzUzAFl5Tg/tCn+ecwYM5ZzCtluBrPTM+uYsKYUInQp/P055g6QXWUgGEyRxGSMPPk9yKm5fC9ZGtqjChpdDnXeEu6gqelzHzbnzvLAIpYqY9POIdz/G74cuWzjKQVB1+g6R2YLY+KzlZFQCOcbNKwB/UB0FySDHox0RPAAAAAElFTkSuQmCC'
        data_atual = 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAK6SURBVFiF7ddbiFVVGAfw3zijEuWMMDpmmnhBDFJD80EffCkvqI+ahA8JRqBShhAEgVApYqFJ0Jsg4lvi5cELPTiohaYiVARdjG7ii4eyBqkYyqaHbx1cZ8/Z58yMY774h83Z67/Xt9b/rO+2Nw9wn9GS3XfgdXQO8x4/4D383UzAHtxAd8aNx6/4t2DXjn/wZ4EfhUdwM+NexGfY10zpIUzLxi/jEo4U5j2JL9M1NuNH4HLabFnGr8D2sk1HNBA0DZ9iUoF/FNfRK06iipF4GF9hSoN1a9DW4Nk2rMHeAt+Nh/AbrmV8L9Zhlv6nVoo8Bj5Ha1poONEh3LK22cRiDAwXhhwD/wvKYuAZbMzG5/G+qBEfCFfBH9iAPryLqZnNNnw7VAHz06bHRartTAImYDReS/OOilO8jaVYnfhXMfNuBEBFVLFiZbyVeGoD9nbGXxVZ0hSNBMzGErW5DhMTT0R4FT9hDFaKOjAXy5PI0lhrze6fw2n8Lnw7F9NFITqOr/GX8PPM9OwyPhbpPEnUjArO4gJ6sBir8D2+a/CHh5yGLTiId0QvqIdxOIFX7oWAN7Cjjqg3C1wbPsKzAxHwAr7BFVHF9if+cRFoV9JVbVitalFtTEVMxkVZBS4Lji68hQUi4B5L/Bh8kvgFok0fEBkwEFwXGTKvmYCBYiHODdLmHBZVB2Vp2Ifn8ZTofH0ZPx+7xItKJ34psW8XbiLc+FK6r6Q1Ggo4gC+y8c/p9yq2CJ/3YI6I8EodAU+UrN1VItqHmFFiVIbN2DRIm4OyE8jfB7YKn3YXLRqgXTSjOQYWiJNxWMRAH7Xpc0nU+Y7+dqXoTdcizYW3iVN+Gz8OYo+mqFbC3aJT1sN4nFSnErb0nztkEVuwHsdEK+9xp3EtFu8Hp+6VgCqq3fBp4cqKKFxnlHyYPMB9x3/x549HgQcqUwAAAABJRU5ErkJggg=='
        
        layout = [
            [sg.Input(f"{valor['-Cartao_Selecionado-']}",disabled=True, size=(10,0), key='-Cartao_Selecionado-')],
            [sg.Text('Mês de Referência', size=(20,0)), sg.Combo(mes, key='-Mes_Referencia-', readonly=True)],
            [sg.Text('Ano de Referência', size=(20,0)), sg.Combo(ano, key='-Ano_Referencia-',  readonly=True, size=(10,0))],
            [sg.Text('Data da Compra', size=(15,0)), sg.Button(key='-Data_Atual-', tooltip='Data Atual', border_width=0, image_data=data_atual, button_color=(sg.theme_background_color(), sg.theme_background_color())), sg.Combo(dia, key='-Dia_Compra-', size=(5,10), default_value='DIA', readonly=True), sg.Combo(mes, key='-Mes_Compra-', default_value='MÊS', readonly=True), sg.Combo(ano, key='-Ano_Compra-', default_value='ANO', readonly=True)],
            [sg.Text('Descrição da Compra', size=(17,0)), sg.Input(size=(35,0), border_width=0, key='-Descricao_Compra-')],
            [sg.Text('Valor da Compra', size=(17,0)), sg.Input(size=(35,0), border_width=0, key='-Valor_Compra-')],
            [sg.Text('Compra parcelada', size=(17,0)), sg.Radio('Sim', 'confirmar1', key='-Parcelar-', enable_events=True), sg.Radio('Não', 'confirmar1', default=True, key='-Nao_Parcelar-', enable_events=True), sg.Combo(vezes, key='-Quant_Parcelas-', readonly=True, visible=False, default_value='Quant Parcelas', size=(14,0))],
            [sg.Text('Comprador', size=(13,0)), sg.Button(key='-Pesquisar_Nomes-', tooltip='Pesquisar Compradores Cadastrados', image_data=btn_pesq, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())), sg.Input(size=(35,0), border_width=0, key='-Comprador-')],
            [sg.Button('Salvar Registro', size=(15,0), border_width=0, key='-Salvar_Registro-'), sg.Text(f'{" "*31}'), sg.Button('Cancelar', size=(15,0), border_width=0, key='-Cancelar-')],
        ]
        
        return sg.Window('Adicionar Registro', layout=layout, finalize=True)
    
    
    def adc_registro_novamente(valor):
        sg.theme('GreenMono')
        dia = []
        for i in range(1, 32):
            dia.append(i)
        vezes = []
        for i in range(2, 25):
            vezes.append(i)
        ano = []
        for i in range(2021, 2030):
            ano.append(i)
        global mes
        mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        
        btn_pesq = 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAAsQAAALEBxi1JjQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAEeSURBVEiJ7dQ5TkMxEMbxXx5HYOmDBBwAjpJNuRBLkx5yiSQ9BwABF2CpAGWBHppHYSNQRIKdKA3ia97ikf8zn2fMv5ZQgTYGeMJbfPbRiusLaxvXKHGLUxzhDHfx/xWqi24+whg1VKbWK6hjgmEupIiZj7HzS+xuhFzKsKstlF9LjG/G+GYqYCB4Pm3LLFVwj96sgOnS9nEes0pRGeMPUgHrgq85GmEjFfCCzUzAFl5Tg/tCn+ecwYM5ZzCtluBrPTM+uYsKYUInQp/P055g6QXWUgGEyRxGSMPPk9yKm5fC9ZGtqjChpdDnXeEu6gqelzHzbnzvLAIpYqY9POIdz/G74cuWzjKQVB1+g6R2YLY+KzlZFQCOcbNKwB/UB0FySDHox0RPAAAAAElFTkSuQmCC'
        data_atual = 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAK6SURBVFiF7ddbiFVVGAfw3zijEuWMMDpmmnhBDFJD80EffCkvqI+ahA8JRqBShhAEgVApYqFJ0Jsg4lvi5cELPTiohaYiVARdjG7ii4eyBqkYyqaHbx1cZ8/Z58yMY774h83Z67/Xt9b/rO+2Nw9wn9GS3XfgdXQO8x4/4D383UzAHtxAd8aNx6/4t2DXjn/wZ4EfhUdwM+NexGfY10zpIUzLxi/jEo4U5j2JL9M1NuNH4HLabFnGr8D2sk1HNBA0DZ9iUoF/FNfRK06iipF4GF9hSoN1a9DW4Nk2rMHeAt+Nh/AbrmV8L9Zhlv6nVoo8Bj5Ha1poONEh3LK22cRiDAwXhhwD/wvKYuAZbMzG5/G+qBEfCFfBH9iAPryLqZnNNnw7VAHz06bHRartTAImYDReS/OOilO8jaVYnfhXMfNuBEBFVLFiZbyVeGoD9nbGXxVZ0hSNBMzGErW5DhMTT0R4FT9hDFaKOjAXy5PI0lhrze6fw2n8Lnw7F9NFITqOr/GX8PPM9OwyPhbpPEnUjArO4gJ6sBir8D2+a/CHh5yGLTiId0QvqIdxOIFX7oWAN7Cjjqg3C1wbPsKzAxHwAr7BFVHF9if+cRFoV9JVbVitalFtTEVMxkVZBS4Lji68hQUi4B5L/Bh8kvgFok0fEBkwEFwXGTKvmYCBYiHODdLmHBZVB2Vp2Ifn8ZTofH0ZPx+7xItKJ34psW8XbiLc+FK6r6Q1Ggo4gC+y8c/p9yq2CJ/3YI6I8EodAU+UrN1VItqHmFFiVIbN2DRIm4OyE8jfB7YKn3YXLRqgXTSjOQYWiJNxWMRAH7Xpc0nU+Y7+dqXoTdcizYW3iVN+Gz8OYo+mqFbC3aJT1sN4nFSnErb0nztkEVuwHsdEK+9xp3EtFu8Hp+6VgCqq3fBp4cqKKFxnlHyYPMB9x3/x549HgQcqUwAAAABJRU5ErkJggg=='
        
        layout = [
            [sg.Input(f"{valor['-Cartao_Selecionado-']}",disabled=True, size=(10,0), key='-Cartao_Selecionado-')],
            [sg.Text('Mês de Referência', size=(20,0)), sg.Combo(mes, key='-Mes_Referencia-', readonly=True, default_value=f'{valor["-Mes_Referencia-"]}')],
            [sg.Text('Ano de Referência', size=(20,0)), sg.Combo(ano, key='-Ano_Referencia-',  readonly=True, size=(10,0), default_value=f'{valor["-Ano_Referencia-"]}')],
            [sg.Text('Data da Compra', size=(15,0)), sg.Button(key='-Data_Atual-', tooltip='Data Atual', border_width=0, image_data=data_atual, button_color=(sg.theme_background_color(), sg.theme_background_color())), sg.Combo(dia, key='-Dia_Compra-', size=(5,10), default_value='DIA', readonly=True), sg.Combo(mes, key='-Mes_Compra-', default_value='MÊS', readonly=True), sg.Combo(ano, key='-Ano_Compra-', default_value='ANO', readonly=True)],
            [sg.Text('Descrição da Compra', size=(17,0)), sg.Input(size=(35,0), border_width=0, key='-Descricao_Compra-')],
            [sg.Text('Valor da Compra', size=(17,0)), sg.Input(size=(35,0), border_width=0, key='-Valor_Compra-')],
            [sg.Text('Compra parcelada', size=(17,0)), sg.Radio('Sim', 'confirmar1', key='-Parcelar-', enable_events=True), sg.Radio('Não', 'confirmar1', default=True, key='-Nao_Parcelar-', enable_events=True), sg.Combo(vezes, key='-Quant_Parcelas-', readonly=True, visible=False, default_value='Quant Parcelas', size=(14,0))],
            [sg.Text('Comprador', size=(13,0)), sg.Button(key='-Pesquisar_Nomes-', tooltip='Pesquisar Compradores Cadastrados', image_data=btn_pesq, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())), sg.Input(size=(35,0), border_width=0, key='-Comprador-')],
            [sg.Button('Salvar Registro', size=(15,0), border_width=0, key='-Salvar_Registro-'), sg.Text(f'{" "*31}'), sg.Button('Cancelar', size=(15,0), border_width=0, key='-Cancelar-')],
        ]
        
        return sg.Window('Adicionar Registro', layout=layout, finalize=True)
    
    
    def filtros():
        sg.theme('GreenMono')
        
        cursor.execute('SELECT comprador FROM registros GROUP BY comprador')
        
        compradores = list()
        for i in cursor.fetchall():
            compradores.append(i)
        
        layout=[
            [sg.Combo(compradores, default_value='COMPRAS POR COMPRADORES', size=(30,5), readonly=True, key='-Comprador-')],
            [sg.Button('Confirmar', key='-Confirmar-', border_width=0, size=(28,0))],
            [sg.Button('Voltar', key='-Voltar-', border_width=0, size=(28,0))]
        ]
        
        return sg.Window('Filtros', layout=layout, finalize=True)
      
    
    def ver_debitos_comprador(valor):
        comprador = valor['-Comprador-'][0]
        cabecalho = Funcoes.COMPRAS_COMPRADORES(valor)[0]
        dados = Funcoes.COMPRAS_COMPRADORES(valor)[1]
        valor_total = Funcoes.COMPRAS_COMPRADORES(valor)[2]
        valor_total = float(valor_total[0])
  
        layout = [
            [sg.Text(f'Compras de {comprador}\nValor Total: R$ {valor_total:.2f}')],
            [sg.Table(values=dados, headings=cabecalho,
                      auto_size_columns=True, 
                      justification='center',
                      num_rows=10,)],
            [sg.Button('Voltar', key='-Voltar-', border_width=0, size=(28,0)),  sg.Button('Gerar Relatório', key='-Gerar_Relatório-', border_width=0, size=(28,0))]
        ]
        
        return sg.Window('Comprador Selecionado', layout=layout, finalize=True)
    
    def edicoes():
        pass
        
class Funcoes:
    def DADOS_FATURA_SELECIONADA(valor):
        fatura_selecionada = valor['-Fatura_Selecionada-'].split('/')
        cursor.execute('SELECT data_compra, descricao_compra, valor_compra, comprador FROM registros WHERE final_cartao = "'+ str(valor['-Cartao_Selecionado-']) +'" AND mes_referencia = "'+ fatura_selecionada[0] +'" and ano_referencia = "'+ fatura_selecionada[1] +'"')
        dados = list()
        for i in cursor.fetchall():
            dados.append(i)
        cabecalho = ['Data da Compra', 'Descrição da Compra', 'Valor da Compra', 'Comprador']
        
        return [cabecalho, dados]
    
    def VENCIMENTO_VALOR_TOTAL(valor):
        fatura_selecionada = valor['-Fatura_Selecionada-'].split('/')
        cursor.execute('SELECT sum(valor_compra) FROM registros WHERE final_cartao = "'+ str(valor['-Cartao_Selecionado-']) +'" AND mes_referencia = "'+ fatura_selecionada[0] +'" and ano_referencia = "'+ fatura_selecionada[1] +'"')
        for i in cursor.fetchall():
            valor_total = i
        valor_total = list(valor_total)
        valor_total = valor_total[0]
        
        valor_total = float(valor_total)
        
        
        cursor.execute('SELECT vencimento from cartoes WHERE final = "'+ str(valor['-Cartao_Selecionado-']) +'"')
        apoio = list(cursor.fetchone())
        vencimento_dia = apoio[0]; vencimento_mes = fatura_selecionada[0]; vencimento_ano = fatura_selecionada[1]
        vencimento = list(); vencimento.append(vencimento_dia); vencimento.append('/'); vencimento.append(vencimento_mes); vencimento.append('/'); vencimento.append(vencimento_ano)
        vencimento = ''.join(vencimento)

        return vencimento, valor_total
    
    def LISTA_COMPRADORES(valor):
        fatura_selecionada = valor['-Fatura_Selecionada-'].split('/')
        cursor.execute('SELECT comprador, ROUND(SUM(valor_compra), 2) FROM registros WHERE final_cartao = "'+ str(valor['-Cartao_Selecionado-']) +'" AND mes_referencia = "'+ fatura_selecionada[0] +'" and ano_referencia = "'+ fatura_selecionada[1] +'" GROUP BY comprador')
        lista_compradores = []  
        for i in cursor.fetchall():
            lista_compradores.append(i)
        cabecalho_comprador = ['Comprador', 'Valor Total']
        return lista_compradores, cabecalho_comprador
            
               
    def COMPRAS_COMPRADORES(valor):
        cabecalho = ['Data da Compra', 'Descrição da Compra', 'Valor da Compra', 'Cartão']
        dados = []
        valor_total = []
        mes_referencia = d.mesAtual()
        mes_referencia -= 1 
        cursor.execute('SELECT data_compra, descricao_compra, valor_compra, final_cartao FROM registros WHERE comprador = "'+ str(valor['-Comprador-'][0]) +'"')
        for i in cursor.fetchall():
            dados.append(i)
        
        cursor.execute('SELECT SUM(valor_compra) FROM registros WHERE comprador = "'+ str(valor['-Comprador-'][0]) +'"')
        for i in cursor.fetchall():
            valor_total = i
        
        return cabecalho, dados, valor_total
        
        
    def PEGAR_NOMES(valor):
        cursor.execute('SELECT comprador FROM registros WHERE final_cartao = "'+ str(valor['-Cartao_Selecionado-']) +'" GROUP BY comprador')
        compradores = []
        for i in cursor.fetchall():
            compradores.append(i)
        
        compradores = list(compradores)
        
        for i in range(len(compradores)):
            print(*compradores[i])
        return compradores
    
    
    def SELECIONAR_FATURA(valor):
        cursor.execute('SELECT mes_referencia, ano_referencia FROM registros  WHERE final_cartao = "'+ str(valor['-Cartao_Selecionado-']) +'" GROUP BY mes_referencia')
        lista = []
        lista_apoio = []
        for i in cursor.fetchall():
            lista_apoio.append(i[0])
            lista_apoio.append('/')
            lista_apoio.append(i[1])
            lista_apoio = ''.join(lista_apoio)
            lista.append(lista_apoio[:])
            lista_apoio = list(lista_apoio)
            lista_apoio.clear()
        
        return lista
    
    
    def ADC_REGISTRO(valor):
        if '' in (valor['-Mes_Referencia-'], valor['-Ano_Referencia-'], valor['-Descricao_Compra-'], valor['-Valor_Compra-'], valor['-Comprador-']) or valor['-Dia_Compra-'] == 'DIA' or valor['-Mes_Compra-'] == 'MÊS' or valor['-Ano_Compra-'] == 'ANO':
            sg.popup('Preencha todos os campos!', title='Campos Incompletos')
        elif valor['-Parcelar-'] and valor['-Quant_Parcelas-'] == 'Quant Parcelas':
            sg.popup('Preencha todos os campos!', title='Campos Incompletos')
        else:
            data_compra = list(); data_compra.append(str(valor['-Dia_Compra-'])); data_compra.append('/'); data_compra.append(str(valor['-Mes_Compra-'])); data_compra.append('/'); data_compra.append(str(valor['-Ano_Compra-']))
            data_compra = ''.join(data_compra)
            try:
                valor['-Valor_Compra-'] = float(valor['-Valor_Compra-'])
            except ValueError:
                sg.popup('Campo de valor preenchido incorretamente\nFormato correto: 000.00', title='Campos incorretos')
            else:
                if valor['-Parcelar-']:
                    cont = mes.index(valor['-Mes_Referencia-'])
                    ano = valor['-Ano_Referencia-']
                    for i in range(0, valor['-Quant_Parcelas-']):
                        cursor.execute('INSERT INTO registros VALUES(null, "'+ str(data_compra) +'", "'+ str(valor['-Descricao_Compra-']) +'", "'+ str(valor['-Valor_Compra-']) +'", "'+ str(valor['-Comprador-']) +'", "'+ mes[cont] +'", "'+ str(ano) +'", "'+ str(valor['-Cartao_Selecionado-']) +'")')
                        cont += 1
                        if cont == 12:
                            cont = 0
                            ano += 1
                    try:
                        bd.commit()
                    except Exception as error:
                        sg.popup_error(f'Erro inesperado ocorrido: {error.__class__}\nErro: {error}', title='Erro Inesperado')
                    else:
                        sg.popup('Dados Inseridos com sucesso', title='Sucesso')
                        return True
                    
                else:
                    try:
                        cursor.execute('INSERT INTO registros VALUES(null, "'+ str(data_compra) +'", "'+ str(valor['-Descricao_Compra-']) +'", "'+ str(valor['-Valor_Compra-']) +'", "'+ str(valor['-Comprador-']) +'", "'+ str(valor['-Mes_Referencia-']) +'", "'+ str(valor['-Ano_Referencia-']) +'", "'+ str(valor['-Cartao_Selecionado-']) +'")')
                        bd.commit()
                    except Exception as error:
                        sg.popup_error(f'Erro inesperado ocorrido: {error.__class__}\nErro: {error}', title='Erro Inesperado')
                    else:
                        sg.popup('Dados Inseridos com sucesso', title='Sucesso')
                        return True
    
    
    def PREENCHER_DATA(janela):
        dia = d.diaAtual(); meses = d.mesAtual(); mes_nome = mes[meses-1]; ano = d.anoAtual()
        janela['-Dia_Compra-'].update(dia); janela['-Mes_Compra-'].update(mes_nome); janela['-Ano_Compra-'].update(ano)
    
    
    def GET_CARTOES():
        cursor.execute('SELECT * FROM cartoes')
        global cartoes
        cartoes = []
        for i in cursor.fetchall():
            cartoes.append(i[1])
        
        return cartoes
    
    
    def QTD_CARTOES():
        cursor.execute('SELECT * FROM cartoes')
        global cartoes
        cartoes = []
        for i in cursor.fetchall():
            cartoes.append(i[1])
        
        return len(cartoes)
    
    def ADC_CARTAO(valor):
        if valor['-Vencimento-'] == '':
            sg.popup('Data de vencimento não preenchida.', title='Vencimento incorreto')
        else:
            try:
                valor['-Adicionar_Cartao-'] = int(valor['-Adicionar_Cartao-'])
            except ValueError:
                sg.popup('Formato incorreto, são aceitos apenas valores númericos.', title='Formato incorreto')
            except Exception as error:
                sg.popup(f'Erro desconhecido: {error.__class__}\n{error}', title='Erro Desconhecido')
            else:
                if valor['-Adicionar_Cartao-'] == '':
                    sg.popup_error('Preencha corretamente o campo\nUltimos 4 digitos do cartão.', title='Preenchimento incorreto')
                elif len(list(str(valor['-Adicionar_Cartao-']))) != 4:
                    sg.popup_error('Preencha corretamente o campo\nUltimos 4 digitos do cartão.', title='Preenchimento incorreto')
                else:
                    cartao = f"Final {valor['-Adicionar_Cartao-']}"
                    cartoes = []
                    cursor.execute('SELECT * FROM cartoes')
                    for i in cursor.fetchall():
                        cartoes.append(i[1])
                    if cartao in cartoes:
                        sg.popup_error('Cartão já cadastrado\nVerifique e tente novamente', title='Cartão já cadastrado')
                    else:
                        try:
                            cursor.execute('INSERT INTO cartoes VALUES (null, "'+ str(cartao) +'", "'+ str(valor['-Vencimento-']) +'")')
                            bd.commit()
                        except Exception as error:
                            sg.popup_error(f'Erro inesperado ocorrido: {error.__class__}\nErro: {error}', title='Erro Inesperado')
                        else:
                            sg.popup('Dados Inseridos com sucesso', title='Sucesso')
                            return True