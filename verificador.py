import pandas as pd
import os
import sys
from datetime import datetime


class VerificadorDuplicados:
    def __init__(self, arquivo_entrada):
        self.arquivo_entrada = arquivo_entrada
        self.df = None
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def carregar_dados(self):
        if not os.path.exists(self.arquivo_entrada):
            print(f"Arquivo '{self.arquivo_entrada}' não encontrado!")
            return False
        
        try:
            self.df = pd.read_excel(self.arquivo_entrada)
            self.df = self.df.map(lambda x: x.strip() if isinstance(x, str) else x)
            print(f"Arquivo carregado: {len(self.df)} registros")
            return True
        except Exception as e:
            print(f"Erro ao carregar arquivo: {e}")
            return False
    
    def encontrar_duplicados(self):
        return self.df[self.df.duplicated(subset=["Nome", "Matrícula"], keep=False)]
    
    def encontrar_dados_faltando(self):
        return self.df[self.df.isnull().any(axis=1)]
    
    def salvar_resultado(self, dados, nome_arquivo):
        if len(dados) > 0:
            os.makedirs("output", exist_ok=True)
            arquivo = f"output/{nome_arquivo}_{self.timestamp}.xlsx"
            dados.to_excel(arquivo, index=False)
            print(f"Salvo: {arquivo}")
            return arquivo
        return None
    
    def executar(self):
        if not self.carregar_dados():
            return False
        
        duplicados = self.encontrar_duplicados()
        dados_faltando = self.encontrar_dados_faltando()
        
        print(f"\nResultados:")
        print(f"- Duplicados: {len(duplicados)}")
        print(f"- Dados faltando: {len(dados_faltando)}")
        
        arquivos_salvos = []
        
        if len(duplicados) > 0:
            arquivo = self.salvar_resultado(duplicados, "duplicados")
            if arquivo:
                arquivos_salvos.append(arquivo)
        
        if len(dados_faltando) > 0:
            arquivo = self.salvar_resultado(dados_faltando, "dados_faltando")
            if arquivo:
                arquivos_salvos.append(arquivo)
        
        if not arquivos_salvos:
            print("Nenhum problema encontrado!")
        
        return True


def criar_dados_exemplo():
    dados = [
        {"Nome": "João Silva", "Matrícula": "2021001", "Curso": "Computação", "Email": "joao@email.com"},
        {"Nome": "Maria Santos", "Matrícula": "2021002", "Curso": "Matemática", "Email": "maria@email.com"},
        {"Nome": "João Silva", "Matrícula": "2021001", "Curso": "Computação", "Email": "joao@email.com"},
        {"Nome": "Pedro Costa", "Matrícula": "2021003", "Curso": None, "Email": "pedro@email.com"},
        {"Nome": "Ana Oliveira", "Matrícula": "2021004", "Curso": "Física", "Email": None},
        {"Nome": "Carlos Lima", "Matrícula": "2021005", "Curso": "Química", "Email": "carlos@email.com"},
    ]
    
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(dados)
    arquivo = "data/alunos_exemplo.xlsx"
    df.to_excel(arquivo, index=False)
    print(f"Dados de exemplo criados: {arquivo}")
    return arquivo


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--criar-exemplo":
        criar_dados_exemplo()
        return
    
    arquivo = "data/alunos_exemplo.xlsx"
    
    if not os.path.exists(arquivo):
        print("Arquivo de exemplo não encontrado. Criando...")
        arquivo = criar_dados_exemplo()
    
    verificador = VerificadorDuplicados(arquivo)
    verificador.executar()


if __name__ == "__main__":
    main()
