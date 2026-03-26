import requests
from .config import COTACAO_PERIODO, COTACAO_DIA

def obtener_cotacoes(inicio, final):
    """
        Obtener cotacoes no periodo especifico
    """

    payload = {
            "@dataInicial":f"'{inicio}'",
            "@dataFinalCotacao":f"'{final}'",
            "$format":"json"
            }

    res = requests.get(COTACAO_PERIODO, params=payload)
    return res.json()


def obtener_cotacao(data):
    """
        Obtener cotacoes dum dia
    """

    payload = {
            "@dataCotacao":f"'{data}'",
            "$format":"json"
            }
    res =  requests.get(COTACAO_DIA,params=payload)
    return res.json()


