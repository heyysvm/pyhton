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

@app.route('/products')
def get_products():
    return products


if __name__ =="__main__":
    app.run(debug=True)