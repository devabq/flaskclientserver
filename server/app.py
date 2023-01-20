from flask import Flask, jsonify, request, redirect
import json
import time

f = open("todos.json")
todosFile = json.load(f)
f.close()

f = open("users.json")
usersFile = json.load(f)
f.close()

app = Flask(__name__)

############
#USER STUFF
############

@app.route("/")
@app.route("/users/")
def default():
    return usersFile


@app.route("/users/<int:userId>/")
def getUserById(userId):
    return usersFile[userId-1]


@app.route("/users/<int:userId>/todos/")
def getUserTodos(userId):
    userTodos= []
    for todo in todosFile:
        if (todo["userId"] == userId):
            userTodos.append(todo)
    return userTodos


@app.route("/users/", methods=["POST"])
def userCreate():
    data = request.get_json()
    data["id"] = len(usersFile) + 1
    usersFile.append(data)
    print(usersFile)
    return json.dumps(data), 201

#############
##TO-DO STUFF
#############

@app.route("/todos/")
def getTodos():
    return todosFile


@app.route("/todos/<int:todoId>/")
def getTodoById(todoId):
    if todoId > len(todosFile):
        return "404"

    else:
        return todosFile[todoId-1]

@app.route("/todos/", methods=["POST"])
def todoCreate():
    data = request.get_json()
    data["id"] = len(todosFile) + 1
    usersFile.append(data)
    print(todosFile)
    return json.dumps(data), 201

if __name__ == "__main__":
    app.run(debug=True)
