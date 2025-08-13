from typing import TypedDict
from decimal import Decimal

class ProductData(TypedDict):
    nome_loja: str
    nome_produto: str
    preco_produto: Decimal
    url_produto: str
    url_foto: str
    status_ativo: bool = True

    def __post_init__(self):
        if not self.nome_loja.strip():
            raise ValueError("Nome da loja não pode ser vazio")
        if not self.nome_produto.strip():
            raise ValueError("Nome do produto não pode ser vazio")
        if self.preco_produto < 0:
            raise ValueError("Preço não pode ser negativo")
        if not self.url_produto.startswith("http"):
            raise ValueError("URL do produto inválida")
        if not self.url_foto.startswith("http"):
            raise ValueError("URL da foto inválida")