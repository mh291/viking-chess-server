from flask import Flask, request, json, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

board = [[{"type":4},{"type":0},{"type":0},{"type":3},{"type":3},{"type":3},{"type":3},{"type":3},{"type":0},{"type":0},{"type":4}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":1},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":1},{"type":1},{"type":1},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":3},{"type":0},{"type":1},{"type":1},{"type":2},{"type":1},{"type":1},{"type":0},{"type":3},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":1},{"type":1},{"type":1},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":1},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":4},{"type":0},{"type":0},{"type":3},{"type":3},{"type":3},{"type":3},{"type":3},{"type":0},{"type":0},{"type":4}]]

currentPlayer = "black"
playerOne = ""
playerTwo = ""
notReadyError = "Both players not yet set"

@app.route("/api/updateBoard", methods=["GET", "POST"])
@cross_origin()
def updateBoard():
    global board, currentPlayer
    if request.method == 'POST':
        if playerOne == "" or playerTwo == "":
            return Response(json.dumps(notReadyError))
        else:
            currentPlayer = "black" if currentPlayer == "white" else "white"
            board = request.data
            return Response(json.dumps("Board updated"))
    else:
        resp = Response(json.dumps(board))
    	return resp

@app.route("/api/currentPlayer", methods=["GET", "OPTIONS"])
@cross_origin()
def getCurrentPlayer(allow_headers=["access-control-allow-origin"]):
    if request.method == 'GET':
        resp = Response(json.dumps(currentPlayer))
        return resp    

@app.route("/api/resetBoard", methods=["POST"])
@cross_origin()
def resetBoard():
    global board, currentPlayer, playerOne, playerTwo
    if request.method == 'POST':
        board = request.data
        currentPlayer = "black"
        playerOne = ""
        playerTwo = ""
        return  Response(json.dumps("Board reset"))

@app.route("/api/setPlayer", methods=["POST"])
@cross_origin()
def setPlayer():
    global currentPlayer, playerOne, playerTwo
    if request.method == 'POST':
        if playerOne == "":
            playerOne = json.loads(request.data)
            return Response(json.dumps(playerOne))
        elif playerTwo == "":
            playerTwo = "white" if playerOne == "black" else "black"
            return Response(json.dumps(playerTwo))
        else:
            return Response(json.dumps("error, two people are already playing"))    

if __name__ == "__main__":
    app.run()