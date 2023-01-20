from flask import Flask, jsonify, request
import json

f = open("todos.json")
todosFile = json.load(f)
f.close()

f = open("users.json")
usersFile = json.load(f)
f.close()

app = Flask(__name__)


@app.route("/")
@app.route("/users/")
def default():
    return jsonify(usersFile)


@app.route("/users/<int:userid>")
def user(userid):
    return jsonify(usersFile[userid-1])


@app.route("/users/<int:userid>/todos")
def usertodos(userid):
    filtered = []
    for todo in todosFile:
        if (todo["userId"] == userid):
            filtered.append(todo)
    return jsonify(filtered)


@app.route("/users/", methods=["POST"])
def update_record():
    record = json.loads(request.data)
    print("==THIS IS A TEST==")
    print(record)
    new_records = []
    return jsonify(record)

@app.route("/todos")
def getTodos():
    return todosFile

if __name__ == "__main__":
    app.run(debug=True)
