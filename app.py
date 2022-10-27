from importsAndConfigs import app
from intermediary.intermediaryMatch import IntermediaryMatch
from intermediary.intermediaryUser import IntermediaryUser
from flask import request, g, jsonify
from flask_cors import cross_origin
from flask_httpauth import HTTPBasicAuth

@app.route('/', methods=['GET'])
def hello():
    return "Service (OK)"

@app.route('/add_new_match', methods=['POST'])
def add_new_match():
    return IntermediaryMatch.add_new_match()

@app.route('/api/register', methods=['POST'])
def register():
    return IntermediaryUser.register()

@app.route('/api/login')
@auth.login_required
def get_token():
    token = g.user.generate_auth_token(600)
    return jsonify({ 'token': token.decode('ascii'), 'duration': 600 })

@app.route('/api/dothis', methods=['GET'])
@auth.login_required
def do_this():
    return jsonify({ 'message':'It is done {}'.format(g.user.username) })

if __name__=='__main__':
	app.run(debug=True) 