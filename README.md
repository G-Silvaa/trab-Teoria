# Verificador de Duplicados

Sistema para detectar registros duplicados e dados faltando em planilhas Excel.

## Uso

```bash

./setup.sh


./start.sh
```

## Arquivo Principal

`verificador.py` - Contém toda a lógica do sistema

### Opções:
- `python verificador.py` - Executa verificação
- `python verificador.py --criar-exemplo` - Cria dados de exemplo

## Estrutura

```
├── verificador.py    # Código principal
├── data/            # Arquivos de entrada
├── output/          # Resultados
├── setup.sh         # Configuração
├── start.sh         # Execução
└── requirements.txt # Dependências
```

## Funcionalidades

- Detecção de duplicados por Nome e Matrícula
- Identificação de campos vazios
- Relatórios em Excel com timestamp
- Criação automática de dados de exemplo
