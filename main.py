import pandas as pd 
import datetime
from datetime import datetime

def corrigir_cnpj(cnpj):
    cnpj = cnpj.replace(',','').replace('/','').replace('-','').replace('.','')
    return cnpj


def busca_informes_cvm_intervalo(ano_inicio, mes_inicio, ano_fim, mes_fim):
    def busca_informes_cvm(ano, mes):
        url = 'https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{:04d}{:02d}.zip'.format(ano, mes)
        return pd.read_csv(url, sep=';', compression='zip', usecols=['CNPJ_FUNDO', 'DT_COMPTC', 'VL_QUOTA'])

    data_inicio = datetime(ano_inicio, mes_inicio, 1)
    data_fim = datetime(ano_fim, mes_fim, 1)

    lista_dados = []

    while data_inicio <= data_fim:
        try:
            dados_mes = busca_informes_cvm(data_inicio.year, data_inicio.month)
            lista_dados.append(dados_mes)
        except Exception as e:
            print(f"Erro ao buscar dados para {data_inicio.year}-{data_inicio.month}: {e}")

        if data_inicio.month == 12:
            data_inicio = datetime(data_inicio.year + 1, 1, 1)
        else:
            data_inicio = datetime(data_inicio.year, data_inicio.month + 1, 1)

    dados_cvm = pd.concat(lista_dados, ignore_index=True)

    return dados_cvm


dadosbrutos = busca_informes_cvm_intervalo(2022, 1, 2024, 7)

dadosbrutos['CNPJ_FUNDO'] = dadosbrutos['CNPJ_FUNDO'].apply(corrigir_cnpj)
dadoscvm = dadosbrutos
dadoscvm['DT_COMPTC'] = pd.to_datetime(dadoscvm['DT_COMPTC'], format='%Y-%m-%d')
dadoscvm = dadoscvm.rename(columns={'DT_COMPTC': 'DATA_COTACAO', 'VL_QUOTA' : 'VALOR_COTA'})


