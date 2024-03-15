import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

PRODUCT_SERVICE_URL = "https://product-service-2ki2.onrender.com" 

carts = {}

def make_product_service_request(endpoint, method="GET", data=None):
    url = f"{PRODUCT_SERVICE_URL}/{endpoint}"
    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url, json=data)
    return response

# Endpoint 1: Retrieve contents of a user's cart
@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    if user_id not in carts:
        return jsonify({"message": "Cart is empty"}), 200
    return jsonify(carts[user_id])

# Endpoint 2: Add a specified quantity of a product to the user's cart
@app.route('/cart/<int:user_id>/add/<int:product_id>', methods=['POST'])
def add_to_cart(user_id, product_id):
    data = request.json
    if "quantity" not in data:
        return jsonify({"error": "Quantity is required"}), 400

    product_response = make_product_service_request(f'/products/{product_id}')
    
    if product_response.status_code == 200:
        product_data = product_response.json()
        product_name = product_data['product']['name']
        product_price = product_data['product']['price']
        
        if user_id not in carts:
            carts[user_id] = {"items": {}}
        
        if product_id in carts[user_id]["items"]:
            carts[user_id]["items"][product_id]["quantity"] += data['quantity']
        else:
            carts[user_id]["items"][product_id] = {
                "name": product_name,
                "quantity": data['quantity'],
                "price": product_price,
            }
        
        return jsonify({"message": f"Product {product_id} added to cart", "cart": carts[user_id]}), 201
    else:
        return jsonify({"error": "Product not found"}), 404

# Endpoint 3: Remove a specified quantity of a product from the user's cart
@app.route('/cart/<int:user_id>/remove/<int:product_id>', methods=['DELETE'])
def remove_from_cart(user_id, product_id):
    data = request.json
    if "quantity" not in data:
        return jsonify({"error": "Quantity is required"}), 400

    if user_id not in carts or product_id not in carts[user_id]["items"]:
        return jsonify({"error": "Product not found in the cart"}), 404

    current_quantity = carts[user_id]["items"][product_id]["quantity"]
    
    if data["quantity"] >= current_quantity:
        del carts[user_id]["items"][product_id]
    else:
        carts[user_id]["items"][product_id]["quantity"] -= data["quantity"]

    return jsonify({"message": f"Product {product_id} removed from cart", "cart": carts[user_id]}), 200

# Endpoint 4: Remove all contents from a user's cart
@app.route('/cart/<int:user_id>/clear', methods=['DELETE'])
def clear_cart(user_id):
    if user_id not in carts:
        return jsonify({"error": "Cart not found for the user"}), 404

    carts[user_id]["items"] = {}

    return jsonify({"message": "Cart cleared successfully", "cart": carts[user_id]}), 200

if __name__ == '__main__':
    app.run(debug=True)
