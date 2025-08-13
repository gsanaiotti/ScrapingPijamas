from .models import Product
from .types import ProductData

def save_product_from_data (data: ProductData) -> Product:



    product, created  = Product.objects.update_or_create(
        nome_loja=data.nome_loja,
        nome_produto=data.nome_produto,
        defaults={
            "preco_produto": data.preco_produto,
            "url_produto": data.url_produto,
            "url_foto": data.url_foto,
            "ativo": data.ativo,
        }
    )
    return product