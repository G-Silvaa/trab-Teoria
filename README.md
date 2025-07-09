# trab-Teoria


# Checagem de Duplicados em Planilhas - TCOMP 2025.1

## Objetivo
Detectar registros duplicados e campos faltando em planilhas de alunos.

## Funcionalidades
- Detecta linhas duplicadas com base em **Nome** e **Matrícula**.
- Identifica linhas com **valores faltando** (células vazias).
- Exporta dois arquivos de resultado:
  - `duplicados_encontrados.xlsx`
  - `dados_faltando.xlsx`

## Requisitos
- Python 3.x
- Bibliotecas: `pandas`, `openpyxl`

## Como usar
1. Instale as dependências:
   ```bash
   pip install pandas openpyxl
   ```

2. Execute o script:
   ```bash
   python verifica_duplicados.py
   ```
