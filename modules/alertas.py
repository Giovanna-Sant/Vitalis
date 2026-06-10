from modules.igse import classificar_risco

class GerenciadorAlertas:
    def __init__(self, pilha_historico, fila_atendimento):
        self._historico = pilha_historico
        self._fila = fila_atendimento

    def emitir_alertas(self, regioes: list) -> list[str]:
        alertas_emitidos = []

        for regiao in regioes:
            igse = regiao.get("igse", 0)
            if igse >= 70:
                mensagem = (
                    f"{regiao['nome']} | IGSE: {igse:.1f} | "
                    f"{classificar_risco(igse)}"
                )
                self._historico.empilhar(mensagem)
                self._fila.enfileirar(mensagem)
                alertas_emitidos.append(mensagem)

        return alertas_emitidos