import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Replace with the actual URL of the Product Service
PRODUCT_SERVICE_URL = "http://product-service-host:port"

# Sample user cart data
user_carts = {}

# Endpoint to retrieve the current contents of a user's shopping cart
@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    user_cart = user_carts.get(user_id, {})
    cart_contents = []

    for product_id, quantity in user_cart.items():
        product_info = get_product_info(product_id)
        if product_info:
            total_price = product_info["price"] * quantity
            cart_contents.append({
                "product_id": product_id,
                "product_name": product_info["name"],
                "quantity": quantity,
                "total_price": total_price,
            })

    return jsonify(cart_contents)

# Endpoint to add a specified quantity of a product to the user's cart
@app.route('/cart/<int:user_id>/add/<int:product_id>', methods=['POST'])
def add_to_cart(user_id, product_id):
    quantity_to_add = int(requests.args.get('quantity', 1))
    user_cart = user_carts.setdefault(user_id, {})
    user_cart[product_id] = user_cart.get(product_id, 0) + quantity_to_add

    return jsonify({"message": "Product added to cart successfully"})

# Endpoint to remove a specified quantity of a product from the user's cart
@app.route('/cart/<int:user_id>/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(user_id, product_id):
    quantity_to_remove = int(requests.args.get('quantity', 1))
    user_cart = user_carts.get(user_id, {})

    if product_id in user_cart:
        user_cart[product_id] = max(user_cart[product_id] - quantity_to_remove, 0)
        if user_cart[product_id] == 0:
            del user_cart[product_id]

        return jsonify({"message": "Product removed from cart successfully"})
    else:
        return jsonify({"error": "Product not found in cart"}), 404

def get_product_info(product_id):
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
