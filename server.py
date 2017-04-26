from flask import Flask, request, json, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

gameList = []
gameCounter = -1
initGameState = {
    'board': None,
    'currentPlayer': "black",
    'playerOne': "",
    'playerTwo': "",
    'winner': "",
    'numPlayers': 1
}

@app.route("/api/updateBoard/<id>", methods=["GET", "POST"])
@cross_origin()
def updateBoard(id):
    global gameList
    id = int(id)
    playerOne = gameList[id]['playerOne']
    playerTwo = gameList[id]['playerTwo']
    board = gameList[id]['board']
    currentPlayer = gameList[id]['currentPlayer']

    if request.method == 'POST':
        if playerOne == "" or playerTwo == "":
            return Response(json.dumps("Both players not yet set"))
        else:
            currentPlayer = "black" if currentPlayer == "white" else "white"
            board = request.data
            gameList[id]['currentPlayer'] = currentPlayer
            gameList[id]['board'] = board
            return Response(json.dumps("Board updated"))
    elif request.method == 'GET':
        return Response(json.dumps(board))    	

@app.route("/api/currentPlayer/<id>", methods=["GET"])
@cross_origin()
def getCurrentPlayer(id):
    id = int(id)
    currentPlayer = gameList[id]['currentPlayer']
    if request.method == 'GET':
        return Response(json.dumps(currentPlayer))

@app.route("/api/resetBoard/<id>", methods=["GET", "POST"])
@cross_origin()
def resetBoard(id):
    global gameList
    id = int(id)
    if request.method == 'GET':
        playerOne = gameList[id]['playerOne']
        playerTwo = gameList[id]['playerTwo'] 
        if playerOne == "" and playerTwo == "":
            return Response(json.dumps("true"))
        else:
            return Response(json.dumps("false"))
    elif request.method == 'POST':
        resetGameState = {
            'board': request.data,
            'currentPlayer': "black",
            'playerOne': "",
            'playerTwo': "",
            'winner': "",
            'numPlayers': gameList[id]['numPlayers']
        }
        gameList[id] = resetGameState
        return Response(json.dumps("Board reset"))

@app.route("/api/setPlayer/<id>", methods=["POST"])
@cross_origin()
def setPlayer(id):
    global gameList
    id = int(id)
    playerOne = gameList[id]['playerOne']
    playerTwo = gameList[id]['playerTwo']
    currentPlayer = gameList[id]['currentPlayer']

    if request.method == 'POST':
        if playerOne == "":
            playerOne = json.loads(request.data)
            gameList[id]['playerOne'] = playerOne
            return Response(json.dumps(playerOne))
        elif playerTwo == "":
            playerTwo = "white" if playerOne == "black" else "black"
            gameList[id]['playerTwo'] = playerTwo
            return Response(json.dumps(playerTwo))
        else:
            return Response(json.dumps("error, two people are already playing"))    

@app.route("/api/winner/<id>", methods=["GET", "POST"])
@cross_origin()
def updateWinner(id):
    global gameList
    id = int(id)
    winner = gameList[id]['winner']

    if request.method == 'POST':
        gameList[id]['winner'] = request.data        
        return Response(json.dumps("Winner Set"))
    else:
        return Response(json.dumps(winner))

@app.route("/api/id/", methods=["GET"])
@cross_origin()
def assignId():
    global gameCounter, gameList

    if request.method == 'GET':
        if len(gameList) > 0 and gameList[len(gameList) - 1]['numPlayers'] < 2:
            gameList[len(gameList) - 1]['numPlayers'] += 1
        else:
            gameList.append(initGameState)
            gameCounter += 1
        resp = Response(json.dumps(gameCounter))
        return resp

if __name__ == "__main__":
    app.run()