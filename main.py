import sqlite3
import PySimpleGUI as sg
from sistemas import Telas as t, Funcoes as f

bd = sqlite3.connect('dados.db')
cursor = bd.cursor()

try:
    cursor.execute('CREATE TABLE cartoes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, final TEXT NOT NULL, vencimento TEXT NOT NULL)')
except sqlite3.OperationalError:
    pass
except Exception as error:
    sg.popup_error(f'Erro inesperado ocorrido: {error.__class__}\n{error}', title='Erro Inesperado')
else:
    try:
        cursor.execute('CREATE TABLE registros (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, data_compra TEXT NOT NULL, descricao_compra TEXT NOT NULL, valor_compra TEXT NOT NULL, comprador TEXT NOT NULL, mes_referencia TEXT NOT NULL, ano_referencia TEXT NOT NULL, final_cartao TEXT NOT NULL)')
    except sqlite3.OperationalError:
        pass
    except Exception as error:
        sg.popup_error(f'Erro inesperado ocorrido: {error.__class__}\n{error}', title='Erro Inesperado')
    else:
        sg.popup('Banco de dados criado com sucesso!', title='Sucesso')


qtd_cartoes = f.QTD_CARTOES()

tela_principal, tela_adc_cartoes, tela_adc_registros = None, None, None
tela_ver_fatura, tela_ver_fatura_selecionada, tela_filtros = None, None, None
tela_ver_debitos_comprador = None

if qtd_cartoes == 0:
    tela_adc_cartoes = t.adc_cartao()
else:
    tela_principal = t.tela_principal()

while True:
    janela, evento, valor = sg.read_all_windows()
    
    if evento == sg.WIN_CLOSED:
        break 
    
    if janela == tela_adc_cartoes and evento == '-Incluir_Cartao-':
        validar = f.ADC_CARTAO(valor)
        if validar == True:
            if sg.popup('Deseja incluir um novo cartão ?', custom_text=('Sim', 'Não')) == 'Sim':
                pass
            else:
                tela_adc_cartoes.hide()
                tela_principal = t.tela_principal()
    
    if janela == tela_principal and evento == '-Novo_Cartao-':
        tela_principal.Hide()
        tela_adc_cartoes = t.adc_cartao()
    
    if janela == tela_adc_cartoes and evento == '-Cancelar-':
        qtd_cartoes = f.QTD_CARTOES()
        if qtd_cartoes == 0:
            if sg.popup('Não existem cartões cadastrados\nDeseja cadastrar um cartão ?', title='Erro', custom_text=('Sim', 'Não')) == 'Sim':
                pass
            else:
                tela_adc_cartoes.hide()
                tela_principal.UnHide()
        else:
            tela_adc_cartoes.hide()
            tela_principal.UnHide()
    
    if janela == tela_adc_registros and evento == '-Cancelar-':
        tela_adc_registros.hide()
        tela_principal.UnHide()  
        
    if janela == tela_principal and evento == '-Adc_Registro-':
        if valor['-Cartao_Selecionado-'] == 'SELECIONAR CARTÃO':
            sg.popup('Selecione um cartão.', title='Cartão Inválido')
        else:
            tela_principal.hide()
            tela_adc_registros = t.adc_registro(valor)
    
    if janela == tela_adc_registros and evento == '-Data_Atual-':
        f.PREENCHER_DATA(tela_adc_registros)

    if janela == tela_adc_registros and evento == '-Salvar_Registro-':
        validar = f.ADC_REGISTRO(valor)
        if validar == True:
            if sg.popup('Deseja adicionar mais um registro nesse cartão ?', custom_text=('Sim', 'Não'), title='Adicionar mais Registros') == 'Sim':
                tela_adc_registros.close()
                tela_adc_registros = t.adc_registro_novamente(valor)
            else:
                tela_adc_registros.close()
                tela_principal.UnHide()
        
    if janela == tela_adc_registros:
        if valor['-Parcelar-']:
            janela['-Quant_Parcelas-'].update(visible=True)
        else:
            janela['-Quant_Parcelas-'].update(visible=False)
    
    if janela == tela_adc_registros and evento == '-Pesquisar_Nomes-':
        compradores = f.PEGAR_NOMES(valor)
        sg.popup('Compradores Cadastrados', *compradores, title='Nomes Cadastrados')    
    
    if janela == tela_principal and evento == '-Ver_Fatura-':
        if valor['-Cartao_Selecionado-'] == 'SELECIONAR CARTÃO':
            sg.popup('Selecione um cartão.', title='Cartão Inválido')
        else:
            tela_principal.hide()
            tela_ver_fatura = t.ver_fatura(valor)
    
    if janela == tela_ver_fatura and evento == '-Confirmar-':
        if valor['-Fatura_Selecionada-'] == 'SELECIONAR FATURA':
            sg.popup('Selecione uma fatura.', title='Cartão Inválido')
        else:
            tela_ver_fatura.close()
            tela_ver_fatura_selecionada = t.ver_fatura_selecionada(valor)
                

    if janela == tela_ver_fatura and evento == '-Cancelar-':
        tela_ver_fatura.close()
        tela_principal.UnHide()
        
    if janela == tela_ver_fatura_selecionada and evento == '-Voltar-':
        tela_ver_fatura_selecionada.close()
        tela_principal.UnHide()

    if janela == tela_principal and evento == '-Filtros-':
        tela_principal.hide()
        tela_filtros = t.filtros()
        
    if janela == tela_filtros and evento == '-Voltar-':
        tela_filtros.close()
        tela_principal.UnHide()
    
    if janela == tela_ver_debitos_comprador and evento == '-Voltar-':
        tela_ver_debitos_comprador.close()
        tela_principal.UnHide()
        
    if janela == tela_filtros and evento =='-Confirmar-':
        if valor['-Comprador-'] == 'COMPRAS POR COMPRADORES':
            sg.popup('Selecione um comprador.', title='Comprador Inválido')
        else:
            tela_filtros.close()
            tela_ver_debitos_comprador = t.ver_debitos_comprador(valor)
            