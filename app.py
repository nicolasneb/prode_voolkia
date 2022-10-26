from importsAndConfigs import app
from flask import request
from flask_cors import cross_origin

@app.route('/', methods=['GET'])
def hello():
    return "Service (OK)"

if __name__=='__main__':
	app.run(debug=True) 