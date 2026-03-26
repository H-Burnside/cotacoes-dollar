import os
API_BASE = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata"

MOEDAS = f"{API_BASE}/Moedas"
COTACAO_DIA = f"{API_BASE}/CotacaoDolarDia(dataCotacao=@dataCotacao)"
COTACAO_PERIODO = f"{API_BASE}/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS_PATH = os.path.join(filepath,"dados","cotacoes.csv")
DIAS_DA_SEMANA = ['SEG','TER','QUA','QUI','SEX','SAB','DOM']
