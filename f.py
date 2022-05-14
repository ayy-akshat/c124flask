import json
from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [
    {
        "id": 1,
        "name": "something",
        "number": "1231231234"
    },
]

@app.route("/")
def hello():
    return "hello"

@app.route("/add_contact", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({"status": "error", "message": "arguments must be in json!"}, 400)
    if (not "name" in request.json.keys() or
        not "number" in request.json.keys()
        ):
        return jsonify({"status": "error", "message": "some data was not provided. please provide 'name' and 'number'."}, 400)
    
    c = {
        "id": contacts[-1]["id"] + 1,
        "name": request.json["name"],
        "number": request.json["number"]
    }
    contacts.append(c)
    return jsonify({"status": "success", "message": "appended contact with name, '" + request.json["name"] + "' and number, '" + request.json["number"] + "'."}, 200)

@app.route("/get_contacts")
def get_contacts():
    return jsonify({"data": contacts})

if (__name__ == "__main__"):
    app.run(debug=True)