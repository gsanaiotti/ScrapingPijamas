from typing import TypedDict

class ProductData(TypedDict):
    nome_loja: str
    nome_produto: str
    id_produto_site: str
    preco_produto: float
    foto_url: str