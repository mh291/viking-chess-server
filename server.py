from flask import Flask, request, json, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

initialBoard = [[{"type":4},{"type":0},{"type":0},{"type":3},{"type":3},{"type":3},{"type":3},{"type":3},{"type":0},{"type":0},{"type":4}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":1},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":1},{"type":1},{"type":1},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":3},{"type":0},{"type":1},{"type":1},{"type":2},{"type":1},{"type":1},{"type":0},{"type":3},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":1},{"type":1},{"type":1},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":1},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":4},{"type":0},{"type":0},{"type":3},{"type":3},{"type":3},{"type":3},{"type":3},{"type":0},{"type":0},{"type":4}]]

board = initialBoard

@app.route("/api/updateBoard", methods=["GET", "POST"])
@cross_origin()
def updateBoard():
    global board
    if request.method == 'POST':
        board = request.data
        print "board updated"
    	return "POSTPOST"
    else:
        resp = Response(json.dumps(board))
    	return resp

@app.route("/api/resetBoard", methods=["POST"])
@cross_origin()
def resetBoard():
    global board
    if request.method == 'POST':
        board = request.data
        print "board reset"
    	return "POSTPOST"

if __name__ == "__main__":
    app.run()