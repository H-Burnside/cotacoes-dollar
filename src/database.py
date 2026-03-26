import csv
import datetime
from .config import DADOS_PATH, DIAS_DA_SEMANA
from .bcb_client import obtener_cotacao, obtener_cotacoes

def criar_dataobject(dt):
    ano ,mes, dia = [int(i) for i in dt.split('-')]
    return datetime.date(ano,mes,dia).isoweekday()
def formatar_dados(data1,data2):
    # Obtener json
    if not data2:
        dados = obtener_cotacao(data1)
    else:
        dados = obtener_cotacoes(data1,data2)

    # Reformando o json
    if dados['value']==[]:
        return "No useful data to show"
    else:
        for item in dados['value']:
            # Obteniendo a data certa para deixar seu dia da semana
            data = item.pop('dataHoraCotacao')
            data = data[:data.index(' ')]
            dia = DIAS_DA_SEMANA[criar_dataobject(data)-1]
            item['diaDaSemana'] = dia
            item['dataCotacao'] = data
    return dados["value"]

def escrever_dados(data1,data2):
    dados = formatar_dados(data1,data2)
    fieldnames = ['dataCotacao', 'cotacaoCompra', 'cotacaoVenda', 'diaDaSemana']
    with open(DADOS_PATH,'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(dados)


if __name__=="__main__":
    escrever_dados("01-01-2025","03-25-2026")
