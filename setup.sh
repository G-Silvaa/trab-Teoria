
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt

python verificador.py --criar-exemplo
python verificador.py
echo "ESTRUTURA DO PROJETO"
echo "============================================================"
echo "src/          - Código fonte"
echo "data/         - Planilhas de entrada"
echo "output/       - Arquivos de saída"
echo "tests/        - Testes"
echo "docs/         - Documentação"
echo ""
echo "Projeto organizado e executado com sucesso!"
