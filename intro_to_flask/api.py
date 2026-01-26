from flask import Flask,request
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

@app.route('/products/search/<query>')
def get_product_by_search(query):
    for product in products:
        if product['name'].lower().startswith(query.lower()): 
            return product
    return {"Error : Product Not Found"} 

@app.route('/add_product',methods=['POST'])
def add_product():
    product = request.get_json()
    
    product['id'] =products[-1]['id']+1
    products.append(product)
    return{'message':'product added successfully','product':product}
    

# @app.route('/products/search')
# def search_products():
#     query = request.args.get("q", "")
#     results = []

#     for product in products:
#         if product['name'].lower().startswith(query.lower()):
#             results.append(product)

#     return {"results": results}


if __name__ =="__main__":
    app.run(debug=True)
    