from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def hello():
	if(request.method == 'POST'):
		return "POSTED"
	else:
		return "GET"

if __name__ == "__main__":
    app.run()