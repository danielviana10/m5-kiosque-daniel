from menu import products


def calculate_tab(list):
    values = []

    for prod in list:
        for product in products:
            if (prod["_id"] == product["_id"]):
                values.append(product["price"] * prod["amount"])
    subtotal = sum(values, start=0)
    return {'subtotal': '${}'.format(round(subtotal, 2))}
