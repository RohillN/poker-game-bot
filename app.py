from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from bot_move import *

app = Flask(__name__)
CORS(app)


# route for index page, status 200 for success
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return "<h1>Poker Bot</h1><h3>Status: Active</h3><p>You can start making post request to: /bot-move</p>"

@app.route('/bot-move', methods=['POST'])
def Post_Cards(cards=None):
    if request.method == 'POST':
        data = request.json
        handlers = {
	        "bluffer": Bluffer(),
	        "risker": Risker(),
	        "conservative": Conservative()
            }
        bot = handlers[data['botType']].handle(data['roomId'], data['botType'], data['balance'], data['lastBetAmount'], data['roundNumber'], data['cardLength'])
        newData = {"name": data['name'], 
                   "uid": data['uid'],
                   "roomId": data['roomId'], 
                   "botType": data['botType'],
                   "newTotalBalance" : bot['balance'],
                   "botMove": bot['move'],
                   "botBetAmount": bot['betAmount'],
                }
        return json.dumps(newData)    

if __name__ == "__main__":
    #	app.run(host='0.0.0.0', port=80)
    app.run(debug=True)
