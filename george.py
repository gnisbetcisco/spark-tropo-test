#import pyCiscoSpark
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello world"

'''
@app.route("/init", methods = ['GET'])
def init():
	at = request.args.get('auth', '')
	print(at)
	return "Bearer " + at
	#pyCiscoSpark.post_createroom()


@app.route("/webhook", methods = ['POST'])
def webhook():
	return request
'''

if __name__ == "__main__":
    app.run()