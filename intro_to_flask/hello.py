from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/name')
def get_name():
    return "Shivam"

@app.route('/name/status')
def get():
    return "this is a another folder in root directory"
if (__name__=='__main__'):
    app.run(debug=True)