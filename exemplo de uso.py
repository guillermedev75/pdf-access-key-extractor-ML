from access_key_extractor import ExtractAccessKey

# Substitua 'caminho_para_nota_fiscal.pdf' pelo caminho do seu arquivo PDF
pdf_path = 'caminho_para_nota_fiscal.pdf'

# Extrai a chave de acesso
access_key = ExtractAccessKey(pdf_path)

# Exibe a chave de acesso
print(f'A chave de acesso é: {access_key}')