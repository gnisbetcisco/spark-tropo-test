from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
    
@app.route("/hello", methods = ['POST'])
def hellogeorge():
	if(request.method == 'POST'):
    	return request
    else:
    	return "A derp"

if __name__ == "__main__":
    app.run()