"""
classificação de igse:
0 - 39: risco baixo
40 - 69: risco medio
70 - 100: risco alto
"""

#peso de cada variável formação do isge
PESOS = {
    "temperatura": 0.25,  # temperaturas extremas afetam saúde cardiovascular
    "umidade": 0.15,      # umidade baixa favorece doenças respiratórias
    "qualidade_ar": 0.35, # poluição do ar é o fator de maior impacto
    "queimadas": 0.25,    # focos de calor elevam partículas no ar
}

#valores máximos esperados
MAXIMOS = {
    "temperatura": 45.0,   # °C — temperatura extrema
    "umidade": 100.0,      # % — inverso: umidade baixa = risco alto
    "qualidade_ar": 300.0, # AQI — índice de qualidade do ar (0-300+)
    "queimadas": 50.0,     # nº de focos registrados na região
}


def normalizar(valor: float, chave: str) -> float:
    maximo = MAXIMOS.get(chave, 100.0)
    normalizado = min(valor / maximo, 1.0) * 100

    #inverte so a umidade pq quanto maior a umidade menos risco
    if chave == "umidade":
        normalizado = 100 - normalizado

    return normalizado


def calcular_igse(regiao: dict) -> float:
    igse = 0.0
    try:
        for chave, peso in PESOS.items():
            valor = float(regiao.get(chave, 0))
            contrib = normalizar(valor, chave) * peso
            igse += contrib
    except (ValueError, TypeError) as e:
        print(f"Erro ao calcular IGSE para '{regiao.get('nome', '?')}': {e}")
        igse = 0.0

    return round(igse, 2)


def classificar_risco(igse: float) -> str:
    if igse >= 70:
        return "ALTO"
    elif igse >= 40:
        return "MODERADO"
    else:
        return "BAIXO"
