
import pandas as pd

# Caminho da planilha de entrada
ARQUIVO_ENTRADA = "alunos_100_exemplo.xlsx"

# Lê a planilha
df = pd.read_excel(ARQUIVO_ENTRADA)

# Remove espaços em branco extras (opcional)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Verifica duplicados com base em Nome e Matrícula
duplicados = df[df.duplicated(subset=["Nome", "Matrícula"], keep=False)]

# Verifica se há valores ausentes
faltando = df[df.isnull().any(axis=1)]

# Exporta os resultados
duplicados.to_excel("duplicados_encontrados.xlsx", index=False)
faltando.to_excel("dados_faltando.xlsx", index=False)

print("Verificação concluída!")
print(f"{len(duplicados)} linhas duplicadas encontradas.")
print(f"{len(faltando)} linhas com dados faltando.")
print("Resultados salvos em 'duplicados_encontrados.xlsx' e 'dados_faltando.xlsx'.")
