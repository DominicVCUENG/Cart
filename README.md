# Cart Service

This repository contains the code for a Cart Service, which is a part of an online shopping platform. The Cart Service manages the shopping cart functionalities, including adding, removing, and clearing items in the user's cart.

## Features

- **Retrieve Cart**: Get the contents of a user's cart.

- **Add to Cart**: Add a specified quantity of a product to the user's cart.

- **Remove from Cart**: Remove a specified quantity of a product from the user's cart.

- **Clear Cart**: Remove all contents from a user's cart.

## Technologies Used

- **Flask**: Web framework for creating the API endpoints.

- **Flask-CORS**: Handling Cross-Origin Resource Sharing (CORS).

- **Requests**: Making HTTP requests to the Product Service.

## API Endpoints

### Retrieve contents of a user's cart

**Endpoint**: `/cart/<int:user_id>`

**Method**: `GET`

**Description**: Retrieves the contents of the specified user's cart.


### Add a specified quantity of a product to the user's cart

**Endpoint**: `/cart/<int:user_id>/add/<int:product_id>`

**Method**: `POST`

**Description**: Adds a specified quantity of a product to the user's cart.

**Request Body**:

```
{
    "quantity": <quantity>
}
```


### Remove a specified quantity of a product from the user's cart

**Endpoint**: `/cart/<int:user_id>/remove/<int:product_id>`

**Method**: `DELETE`

**Description**: Removes a specified quantity of a product from the user's cart.

**Request Body**:

```
{
    "quantity": <quantity>
}
```

### Remove all contents from a user's cart

**Endpoint**: `/cart/<int:user_id>/clear`

**Method**: `DELETE`

**Description**: Clears all contents from the specified user's cart.


## How to Run

1. Clone the repository:

```
git clone https://github.com/DominicVCUENG/Cart.git
```

2. Navigate to the project directory:

```
cd Cart
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the Flask application:

```
python product.py
```

## Project Structure

- **`cart.py`**: Main Flask application file

- **`requirements.txt `**: Python dependencies

## Example Usage

### Retrieve Cart

```python
import requests

response = requests.get('http://localhost:5000/cart/1')
print(response.json())
```

### Add to Cart

```python
import requests

data = {
    "quantity": 3
}
response = requests.post('http://localhost:5000/cart/1/add/2', json=data)
print(response.json())
```

### Remove from Cart

```python
import requests

data = {
    "quantity": 1
}
response = requests.delete('http://localhost:5000/cart/1/remove/2', json=data)
print(response.json())
```

### Clear Cart

```python
import requests

response = requests.delete('http://localhost:5000/cart/1/clear')
print(response.json())
```
