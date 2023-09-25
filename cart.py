import requests

def get_all_products():
    response = requests.get(f'http://127.0.0.1:5000/products')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error getting products. Status code: {response.status_code}")
        return None

def add_product(id, name, price, quantity):
    new_product = {"id": id, "name": name, "price": price, "quantity": quantity}
    response = requests.post(f'http://127.0.0.1:5000/products', json = new_product)
    if response.status_code == 201:
        data = response.json()
        return data
    else:
        print(f"Error adding product. Status: {response.json()}")
        return None

def remove_product(product_id):
    response = requests.delete(f'http://127.0.0.1:5000/products/{product_id}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error removing product. Status code: {response.status_code}")
        return None


if __name__ == '__main__':

    all_products = get_all_products()
    print("All Products:")
    print(all_products)

    product_id = 1
    product_name = "peaches"
    product_price = .50
    product_quantity = 25

    added_product = add_product(product_id, product_name, product_price, product_quantity)
    print(f"\nAdded Product {product_name}:\n")
    print(added_product)

    all_products = get_all_products()
    print("\nAll Products:\n")
    print(all_products)

    removed_product = remove_product(product_id)
    print(f"\nRemoved Product {product_id}:")
    print(removed_product)

    all_products = get_all_products()
    print("\nAll Products:\n")
    print(all_products)