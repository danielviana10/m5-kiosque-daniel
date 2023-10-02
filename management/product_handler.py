from menu import products


def get_product_by_id(id):
    # if type(id) != int:
    #     raise TypeError("product id must be an int")

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


def add_product(menu, args):
    new_id = 0

    for product in menu:
        if (product["_id"] > new_id):
            new_id = product["_id"]
    add_id = new_id + 1

    _product = {"_id": add_id}

    _product.update(args)

    menu.append(_product)

    return _product
