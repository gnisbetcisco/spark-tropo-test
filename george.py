from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def hello():
	if(request.method == 'POST'):
		return str(request)
	else:
		return "GET"



@app.route("/webhook", methods = ['POST'])
def webhook():
	return request


if __name__ == "__main__":
    app.run()