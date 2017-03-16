from flask import Flask, request, json, Response, make_response

app = Flask(__name__)
board = [[{"type":4},{"type":0},{"type":0},{"type":3},{"type":3},{"type":3},{"type":3},{"type":3},{"type":0},{"type":0},{"type":4}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":1},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":1},{"type":1},{"type":1},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":3},{"type":0},{"type":1},{"type":1},{"type":2},{"type":1},{"type":1},{"type":0},{"type":3},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":1},{"type":1},{"type":1},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":1},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":0},{"type":0},{"type":0},{"type":0},{"type":0},{"type":3},{"type":0},{"type":0},{"type":0},{"type":0},{"type":0}],[{"type":4},{"type":0},{"type":0},{"type":3},{"type":3},{"type":3},{"type":3},{"type":3},{"type":0},{"type":0},{"type":4}]]

@app.route("/api/updateBoard", methods=["GET", "POST"])
def updateBoard():
    if request.method == 'POST':
    	print request.data
    	return "POSTPOST"
    else:
    	return json.dumps(board)

if __name__ == "__main__":
    app.run()