from management import product_handler
from management import tab_handler

if __name__ == "__main__":
    print(product_handler.get_product_by_id(1))
    print(product_handler.get_products_by_type("vegetable"))
    print(product_handler.add_product([], _product={
            "description": "Unsweetened natural orange juice",
            "price": 9.99,
            "rating": 4.5,
            "title": "Orange Juice",
            "type": "juice"
        }
    ))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]
    print(tab_handler.calculate_tab(table_2))
