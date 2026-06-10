def busca_linear(regioes: list, nome: str) -> int | None:
    #complexidade O(n)
    nome_lower = nome.strip().lower()
    for i, regiao in enumerate(regioes):
        if regiao["nome"].strip().lower() == nome_lower:
            return i
    return None

def busca_binaria(lista_ordenada: list, alvo: str) -> int:
    #complexidade: O(log n)
    esquerda = 0
    direita = len(lista_ordenada) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista_ordenada[meio] == alvo:
            return meio
        elif lista_ordenada[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

def merge_sort(valores: list, nomes: list) -> tuple[list, list]:
    #complexidade: O(n log n)
    if len(valores) <= 1:
        return valores, nomes

    meio = len(valores) // 2

    val_esq, nom_esq = merge_sort(valores[:meio], nomes[:meio])
    val_dir, nom_dir = merge_sort(valores[meio:], nomes[meio:])

    return _merge(val_esq, nom_esq, val_dir, nom_dir)

def _merge(val_e, nom_e, val_d, nom_d):
    val_res, nom_res = [], []
    i = j = 0

    while i < len(val_e) and j < len(val_d):
        if val_e[i] <= val_d[j]:
            val_res.append(val_e[i])
            nom_res.append(nom_e[i])
            i += 1
        else:
            val_res.append(val_d[j])
            nom_res.append(nom_d[j])
            j += 1

    val_res.extend(val_e[i:])
    nom_res.extend(nom_e[i:])
    val_res.extend(val_d[j:])
    nom_res.extend(nom_d[j:])

    return val_res, nom_res

def bubble_sort(valores: list, nomes: list) -> tuple[list, list]:
    #complexidade: O(n²)
    n = len(valores)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if valores[j] > valores[j + 1]:
                valores[j], valores[j + 1] = valores[j + 1], valores[j]
                nomes[j], nomes[j + 1] = nomes[j + 1], nomes[j]
                trocou = True
        if not trocou:
            break  #se ja estiver ordenado
    return valores, nomes
