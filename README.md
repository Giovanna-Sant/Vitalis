# 🛰️ VITALIS — Plataforma de Inteligência em Saúde Ambiental

> Projeto desenvolvido para a disciplina de **Estruturas de Dados** — Engenharia de Software, 2º Semestre  
> FIAP · Global Solution 2025 · 1º Semestre de 2026

---

## 📋 Descrição do Projeto

O **Vitalis** é uma aplicação em Python que simula uma plataforma de inteligência em saúde pública baseada em dados ambientais provenientes de satélites de observação da Terra. O sistema coleta, organiza e processa dados como temperatura, umidade, qualidade do ar e focos de queimadas, calculando o **Índice Global de Saúde Espacial (IGSE)** para identificar regiões em risco sanitário e emitir alertas preventivos.

---

## 🎯 Objetivo da Solução

Demonstrar como dados ambientais de satélites podem apoiar a tomada de decisão em saúde pública, identificando regiões de maior risco antes que surtos e eventos sanitários se agravem — integrando estruturas de dados e algoritmos fundamentais para análise, ordenação e busca eficiente das informações.

---

## 🌍 Tema Escolhido

**Monitoramento climático, qualidade do ar e eventos extremos** aplicados à saúde pública.  
O projeto está alinhado ao produto **Vitalis** desenvolvido na disciplina de Agile Methodology with Squad Framework.

---

## 📡 Fonte dos Dados

Os dados utilizados foram construídos com base em referências reais de:

- **INPE** (Instituto Nacional de Pesquisas Espaciais) — focos de queimadas e temperatura
- **NASA FIRMS** (Fire Information for Resource Management System) — monitoramento de queimadas via MODIS
- **Copernicus / Sentinel-5P** — qualidade do ar (AQI)
- **NOAA / GOES-16** — dados meteorológicos
- **IBGE** — coordenadas geográficas das regiões brasileiras

> Os dados estão armazenados no arquivo `data/regioes.csv` com 30 regiões brasileiras.

---

## 🏗️ Estruturas de Dados Implementadas

Todas as estruturas foram implementadas **do zero**, sem uso de bibliotecas externas.

| Estrutura | Arquivo | Uso no Projeto |
|---|---|---|
| **Pilha (LIFO)** | `modules/estruturas.py` | Histórico de alertas emitidos — o alerta mais recente é exibido primeiro |
| **Fila (FIFO)** | `modules/estruturas.py` | Ordem de atendimento — as regiões em risco entram na fila conforme os alertas são emitidos |
| **Lista Ligada Simples** | `modules/estruturas.py` | Registro das regiões monitoradas, com inserção encadeada de nós |

---

## ⚙️ Algoritmos Utilizados

| Algoritmo | Tipo | Complexidade | Uso no Projeto |
|---|---|---|---|
| **Busca Linear** | Busca | O(n) | Localizar região por nome na lista completa |
| **Busca Binária** | Busca | O(log n) | Confirmar a existência em lista ordenada alfabeticamente |
| **Merge Sort** | Ordenação | O(n log n) | Ordenar regiões pelo IGSE de forma eficiente |
| **Bubble Sort** | Ordenação | O(n²) | Ordenação alternativa (didática), com otimização de parada antecipada |

---

## 🧮 Cálculo do IGSE

O **Índice Global de Saúde Espacial** é calculado com pesos ponderados:

```
IGSE = (temperatura_norm × 0,25) + (umidade_norm × 0,15) + (qualidade_ar_norm × 0,35) + (queimadas_norm × 0,25)
```

| Faixa IGSE | Classificação |
|---|---|
| 0 – 39 | 🟢 Risco Baixo |
| 40 – 69 | 🟡 Risco Moderado |
| 70 – 100 | 🔴 Risco Alto |

---

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.10+**
- Biblioteca padrão: `csv`, `os`, `datetime`, `time`
- Sem dependências externas obrigatórias

---

## 📂 Estrutura do Projeto

```
vitalis/
├── main.py                  # Ponto de entrada — menu principal do sistema
├── requirements.txt
├── README.md
├── data/
│   └── regioes.csv          # Base de dados com 30 regiões brasileiras
├── logs/
│   └── sistema.log          # Log automático de execução (gerado em runtime)
└── modules/
    ├── __init__.py
    ├── estruturas.py         # Pilha, Fila e Lista Ligada implementadas do zero
    ├── algoritmos.py         # Busca Linear, Busca Binária, Merge Sort, Bubble Sort
    ├── igse.py               # Cálculo e classificação do IGSE
    ├── dados.py              # Leitura e gravação de arquivos CSV
    ├── alertas.py            # Gerenciador de alertas de risco alto
    └── logs.py               # Sistema de log com timestamp
```

---

## ▶️ Instruções de Execução

### Pré-requisitos

- Python 3.10 ou superior instalado
- Nenhuma biblioteca externa necessária

### Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/vitalis-gs.git
cd vitalis-gs

# Execute o sistema
python main.py
```

### Fluxo recomendado de uso

1. Inicie o sistema
2. **Opção 1** — Carregue os dados do CSV
3. **Opção 2** — Calcule o IGSE de todas as regiões
4. **Opção 3** — Busque uma região específica (ex: `Cuiabá`)
5. **Opção 4** — Ordene por IGSE e compare os algoritmos
6. **Opção 5** — Emita alertas de risco alto
7. **Opções 6, 7, 8** — Explore Pilha, Fila e Lista Ligada
8. **Opção 9** — Visualize o log do sistema

---

## 👥 Integrantes do Grupo

| Nome | RM |
|---|---|
| Anna Clara Ruggeri da Silva | RM565553 |
| Eduardo Viudes Chorro | RM564075 |
| Giovanna da Silva Santos | RM566301 |
| Giovanna Luiza Bento | RM563203 |
| Victor Tadashi Saito Barra | RM563582 |
