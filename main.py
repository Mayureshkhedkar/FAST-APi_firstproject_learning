#first git push
# 
# myenv\Scripts\Activate.ps1   run the command in terminal to activate the virtual environment

from fastapi import FastAPI
from models import Products
app = FastAPI()

@app.get("/")
def greet():
    return "Hello this is my first python code in fastapi"



products = [
    Products(id=1, name="Laptop", description="High-performance laptop", price=999.99, quantity=10),
    Products(id=2, name="Smartphone", description="Latest smartphone", price=499.99, quantity=20),
    Products(id=3, name="Headphones", description="Wireless noise-canceling headphones", price=199.99, quantity=15),
    Products(id=4, name="Smartwatch", description="Stylish smartwatch with fitness tracking", price=299.99, quantity=5),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    
    return "The product with the given id does not exist!"


@app.post("/product")
def create_new_product(product: Products):
    for prod in products:
        if product.id == prod.id:       
            return "The product with the given id already exists! Please choose a different id."
    products.append(product)
    return "Product created successfully!"

@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return "Product deleted successfully!"
    
    return "The product with the given id does not exist!"

@app.put("/product/{product_id}")
def update_product(product_id:int, updated_product:Products):
    for prod in products:
        if prod.id==product_id:
            prod.name=updated_product.name
            prod.description=updated_product.description
            prod.price=updated_product.price
            prod.quantity=updated_product.quantity
            return "Product updated successfully!"
    return "The product with the given id does not exist! and no changes made to the product list"