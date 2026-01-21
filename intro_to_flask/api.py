from flask import Flask 

app = Flask(__name__)

products =[
    {"id":1, "name":"Chopping Board","Price":350},
    {"id":2, "name":"Stickers","Price":200},
    {"id":3, "name":"Mouse","Price":50},
    {"id":4, "name":"Sneakers","Price":1000},
    {"id":5, "name":"Sneakers2","Price":1450}
]

@app.route('/')
def get_load():
    return "Welcome !!"

@app.route('/products', methods=['GET'])
def get_products():
  return products

@app.route('/products/<product_id>')
def get_product(product_id):
    product_id=int(product_id)
    for product in products:
        if product['id']==product_id:
            return product
    return{"error":"Product Not Found"}

@app.route('/products/name/<product_name>')
def get_product_by_name(product_name):
    for product in products:
        if product['name'].lower() == product_name.lower():
            return product
    return {"error": "Product Not Found"}


if __name__ =="__main__":
    app.run(debug=True)