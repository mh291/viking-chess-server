from flask import Flask, request, json, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

board = [[{"type":4},{"type":0},{"type":0},{"type":3},{"type":3},{"type":3},{"type":3},{"type":3},{"type":0},{"type":0},{"type":4}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":1},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":1},{"type":1},{"type":1},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":3},{"type":0},{"type":1},{"type":1},{"type":2},{"type":1},{"type":1},{"type":0},{"type":3},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":1},{"type":1},{"type":1},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":1},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":4},{"type":0},{"type":0},{"type":3},{"type":3},{"type":3},{"type":3},{"type":3},{"type":0},{"type":0},{"type":4}]]

currentPlayer = "black"
playerOne = ""
playerTwo = ""
winner = ""
counter = 1

@app.route("/api/updateBoard", methods=["GET", "POST"])
@cross_origin()
def updateBoard():
    global board, currentPlayer, counter
    if request.method == 'POST':
        if playerOne == "" or playerTwo == "":
            return Response(json.dumps("Both players not yet set"))
        else:
            currentPlayer = "black" if currentPlayer == "white" else "white"
            board = request.data
            return Response(json.dumps("Board updated"))
    elif request.method == 'GET':
        print "\n"
        print board
        print  "\n"
        print counter
        print "\n"
        counter += 1
        return Response(json.dumps(board))    	

@app.route("/api/currentPlayer", methods=["GET", "OPTIONS"])
@cross_origin()
def getCurrentPlayer(allow_headers=["access-control-allow-origin"]):
    if request.method == 'GET':
        return Response(json.dumps(currentPlayer))

@app.route("/api/resetBoard", methods=["GET", "POST"])
@cross_origin()
def resetBoard():
    global board, currentPlayer, playerOne, playerTwo, winner
    if request.method == 'GET':
        if playerOne == "" and playerTwo == "":
            return Response(json.dumps("true"))
        else:
            return Response(json.dumps("false"))
    elif request.method == 'POST':
        board = request.data
        currentPlayer = "black"
        playerOne = ""
        playerTwo = ""
        winner = ""
        return Response(json.dumps("Board reset"))

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

@app.route("/api/winner", methods=["GET", "POST"])
@cross_origin()
def updateWinner():
    global winner
    if request.method == 'POST':
        print request.data
        winner = request.data
        return Response(json.dumps("Winner Set"))
    else:
        return Response(json.dumps(winner))

if __name__ == "__main__":
    app.run()