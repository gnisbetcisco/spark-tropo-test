from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
    
@app.route("/hello", methods = ['POST'])
def hellogeorge():
	
    return request

if __name__ == "__main__":
    app.run()