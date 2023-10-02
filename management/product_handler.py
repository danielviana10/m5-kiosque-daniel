from menu import products
from collections import Counter


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")

    for product in products:
        if (product["_id"] == id):
            return product
    return {}


def get_products_by_type(_type):
    product_array = []

    if type(_type) != str:
        raise TypeError("product type must be a str")

    for product in products:
        if (product["type"] == _type):
            product_array.append(product)
    return product_array


def add_product(menu, **args):
    new_id = 0

    for product in menu:
        if (product["_id"] > new_id):
            new_id = product["_id"]
    add_id = new_id + 1

    _product = {"_id": add_id}

    _product.update(args)

    menu.append(_product)

    return _product


def menu_report():
    product_count = len(products)

    total = sum(product["price"] for product in products)

    average_price = total / product_count

    product_types = Counter(product["type"] for product in products)

    most_common_type = product_types.most_common(1)[0][0]

    return ("Products Count: {0} - Average Price: ${1} - Most Common Type: {2}".format(product_count, round(average_price, 2), most_common_type))
