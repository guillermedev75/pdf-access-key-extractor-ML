# ml_access_key_extractor

Biblioteca para extrair chave de acesso na nota fiscal em PDF.

## Instalação

Você pode instalar esta biblioteca usando pip:

```bash
pip install ml-access-key-extractor
```

## Uso

```python
from access_key_extractor import ExtractAccessKey

# Substitua 'caminho_para_nota_fiscal.pdf' pelo caminho do seu arquivo PDF
pdf_path = 'caminho_para_nota_fiscal.pdf'

# Extrai a chave de acesso
access_key = ExtractAccessKey(pdf_path)

# Exibe a chave de acesso
print(f'A chave de acesso é: {access_key}')
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar pull requests para melhorar esta biblioteca.

## Licença

Este projeto é licenciado sob a [Licença MIT](https://chat.openai.com/c/LICENSE) - veja o arquivo `LICENSE` para detalhes.
