from menu import products


def get_product_by_id(id):
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(type):
    matching_products = [
        product for product in products if product["type"] == type
    ]  # noqa
    return matching_products
