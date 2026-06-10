import csv
import os

cabecalho = ["nome", "temperatura", "umidade", "qualidade_ar", "queimadas", "latitude", "longitude"]

def carregar_dados(caminho: str) -> list[dict]:
    #parametro: path do csv
    #return: lista das regiões com dados
    #tratamento de erro: erro se o arquivo não existir e se algujm campo estiver invalido

    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: '{caminho}'")

    regioes = []

    with open(caminho, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for i, linha in enumerate(leitor, start=2):
            try:
                regiao = {
                    "nome": linha["nome"].strip(),
                    "temperatura": float(linha["temperatura"]),
                    "umidade": float(linha["umidade"]),
                    "qualidade_ar": float(linha["qualidade_ar"]),
                    "queimadas": int(linha["queimadas"]),
                    "latitude": float(linha["latitude"]),
                    "longitude": float(linha["longitude"]),
                }
                regioes.append(regiao)
            except (KeyError, ValueError) as e:
                (f"AVISO: linha {i} inválida no CSV — {e}")
                print(f"AVISO: linha {i} ignorada ({e})")
    return regioes

def salvar_dados(regioes: list[dict], caminho: str) -> None:
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    campos = cabecalho + ["igse"]

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos, extrasaction="ignore")
        escritor.writeheader()
        escritor.writerows(regioes)