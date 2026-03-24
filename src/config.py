API_BASE = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata"

MOEDAS = f"{API_BASE}/Moedas"
COTACOE_DIA = f"{API_BASE}/CotacaoDolarDia(dataCotacao=@dataCotacao)"
COTACAO_PERIODO = f"{API_BASE}/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"

RUTA_DADOS = "../dados/cotacoes.csv"
CSV_HEADERS = "['cotacaoCompra', 'cotacaoVenda', 'dataHoraCotacao','diaDaSemana']
