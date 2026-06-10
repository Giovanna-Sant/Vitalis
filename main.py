import os
import time
from modules.dados import carregar_dados, salvar_dados
from modules.estruturas import Pilha, Fila, ListaLigada
from modules.igse import calcular_igse, classificar_risco
from modules.algoritmos import busca_binaria, busca_linear, merge_sort, bubble_sort
from modules.alertas import GerenciadorAlertas

def menu_principal():
    print("=========================================")
    print("VITALIS - Inteligência em Saúde Ambiental")
    print("Monitoramento via Dados de Satélites")
    print("=========================================")
    print("\n1 - Carregar e exibir dados ambientais")
    print("2 - Calcular IGSE das regiões")
    print("3 - Buscar região por nome")
    print("4 - Ordenar regiões por risco (IGSE)")
    print("5 - Emitir alertas de risco alto")
    print("6 - Histórico de alertas (Pilha)")
    print("7 - Fila de atendimentos prioritários")
    print("8 - Lista de regiões monitoradas (Lista Ligada)")
    print("0 - Sair")
    print()


def main():
    regioes = []
    historico_alertas = Pilha()
    fila_atendimento = Fila()
    lista_regioes = ListaLigada()
    gerenciador = GerenciadorAlertas(historico_alertas, fila_atendimento)

    while True:
        menu_principal()

        try:
            opcao = input("Escolha uma opção: ").strip()
        except KeyboardInterrupt:
            print("\n\nEncerrando o sistema...")
            break

        if opcao == "1":
            print("Carregando dados ambientais")
            time.sleep(0.6)
            print("Carregando dados ambientais.")
            time.sleep(0.6)
            print("Carregando dados ambientais..")
            time.sleep(0.6)
            print("Carregando dados ambientais...")
            try:
                regioes = carregar_dados("data/regioes.csv")
                lista_regioes = ListaLigada()
                for r in regioes:
                    lista_regioes.inserir(r["nome"])
                print(f"{'Região':<20} {'°C Temp': <10} {'% Umid': <10} {'Qualid. Ar':<12} {'Queimadas'}")
                print("-----------------------------------------------------------")
                for r in regioes:
                    print(f"{r['nome']:<20} {r['temperatura']:<10} {r['umidade']:<10} {r['qualidade_ar']:<12} {r['queimadas']}")
                print(f"\n{len(regioes)} regiões carregadas com sucesso!\n")
            except Exception as e:
                print(f"ERRO ao carregar dados: {e}")

        elif opcao == "2":
            print("\n-- Calculo do IGSE - Índice Global de Saúde Espacial --\n")
            if not regioes:
                print("Carregue os dados primeiro (opção 1).")
            else:
                print(f"{'Região':<20} {'IGSE':<8} {'Classificação'}")
                print("-----------------------------------------------------------")
                for r in regioes:
                    igse = calcular_igse(r)
                    r["igse"] = igse
                    classe = classificar_risco(igse)
                    print(f"{r['nome']:<20} {igse:<8.1f} {classe}")

        elif opcao == "3":
            print("\n-- Busca de região --\n")
            if not regioes:
                print("Carregue os dados primeiro (opção 1).")
            else:
                nome = input("Digite o nome da região: ").strip()
                print()

                # busca linear
                resultado_linear = busca_linear(regioes, nome)
                if resultado_linear is not None:
                    print(f"[Busca Linear] Região encontrada na posição {resultado_linear}:")
                    r = regioes[resultado_linear]
                    print(f"Nome        : {r['nome']}")
                    print(f"Temperatura : {r['temperatura']} °C")
                    print(f"Umidade     : {r['umidade']} %")
                    print(f"Qualidade ar: {r['qualidade_ar']}")
                    print(f"Queimadas   : {r['queimadas']}")
                    if "igse"in r:
                        print(f"IGSE        : {r['igse']:.1f} ({classificar_risco(r['igse'])})")
                else:
                    print(f"[Busca Linear] Região '{nome}' não encontrada.")

                #busca linezr
                lista_ordenada = sorted(regioes, key=lambda x: x["nome"].lower())
                nomes_ordenados = [r["nome"].lower() for r in lista_ordenada]
                idx_bin = busca_binaria(nomes_ordenados, nome.lower())
                if idx_bin != -1:
                    print(f"[Busca Binária] Confirmada na lista ordenada (índice {idx_bin}).")
                else:
                    print(f"[Busca Binária] Não encontrada na lista ordenada.")

        elif opcao == "4":
            print("\n-- Lista de IGSE crescente --\n")
            if not regioes:
                print("Carregue os dados primeiro (opção 1).")
            else:
                for r in regioes:
                    if "igse"not in r:
                        r["igse"] = calcular_igse(r)

                print("Escolha o algoritmo de ordenação:")
                print("[1] Merge Sort (eficiente - O(n log n))")
                print("[2] Bubble Sort (didático - O(n²))")
                alg = input("\nOpção: ").strip()

                valores = [r["igse"] for r in regioes]
                nomes = [r["nome"] for r in regioes]

                inicio = time.time()
                if alg == "1":
                    igse_ord, nomes_ord = merge_sort(valores, nomes)
                    metodo = "Merge Sort"
                else:
                    igse_ord, nomes_ord = bubble_sort(valores[:], nomes[:])
                    metodo = "Bubble Sort"
                fim = time.time()

                print(f"\n[{metodo}] Regiões ordenadas por IGSE (maior --> menor):\n")
                print(f"{'#':<5} {'Região':<20} {'IGSE':<8} {'Classificação'}")
                print("---------------------------------------------")
                for i in range(len(igse_ord) - 1, -1, -1):
                    print(f"{len(igse_ord)-i:<5} {nomes_ord[i]:<20} {igse_ord[i]:<8.1f} {classificar_risco(igse_ord[i])}")
                print(f"\nTempo de execução: {(fim - inicio)*1000:.3f} ms")

        elif opcao == "5":
            print("\n-- Emissão de alertas de alto risco--\n")
            if not regioes:
                print("Carregue os dados primeiro (opção 1).")
            else:
                for r in regioes:
                    if "igse"not in r:
                        r["igse"] = calcular_igse(r)
                alertas = gerenciador.emitir_alertas(regioes)
                if alertas:
                    print(f"{len(alertas)} regiões em RISCO ALTO:\n")
                    for a in alertas:
                        print(f"--> {a}")
                else:
                    print("Nenhuma região em risco alto no momento.")
             
        elif opcao == "6":
            print("Histórico de alertas\n")
            if historico_alertas.esta_vazia():
                print("Nenhum alerta registrado ainda.")
            else:
                print("Alertas mais recentes primeiro:\n")
                temp = Pilha()
                i = 1
                while not historico_alertas.esta_vazia():
                    item = historico_alertas.desempilhar()
                    print(f"{i}. {item}")
                    temp.empilhar(item)
                    i += 1
                # restaurar a pilha
                while not temp.esta_vazia():
                    historico_alertas.empilhar(temp.desempilhar())

        elif opcao == "7":
            print("\nFila de atendimentos prioritários\n")
            # fifo - primeiro a entrar e primeiro a sair
            if fila_atendimento.esta_vazia():
                print("Nenhum atendimento na fila.")
            else:
                print("Ordem de atendimento (primeiro a entrar, primeiro a sair):\n")
                temp_lista = []
                while not fila_atendimento.esta_vazia():
                    item = fila_atendimento.desenfileirar()
                    temp_lista.append(item)
                for i, item in enumerate(temp_lista, 1):
                    print(f"{i}. {item}")
                    fila_atendimento.enfileirar(item)

        elif opcao == "8":
            print("\nLista de regiões monitoradas\n")
            #lista ligada
            if lista_regioes.esta_vazia():
                print("Carregue os dados primeiro (opção 1).")
            else:
                lista_regioes.exibir()

        elif opcao == "0":
            print("\nEncerrando o Vitalis. Até logo!\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()