from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.method
    else:
        return request.method

if __name__ == "__main__":
    app.run()