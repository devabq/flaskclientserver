from flask import Flask, request, render_template
import users
import todos

app = Flask(__name__)

usersApp = users.Users()
todosApp = todos.Todos()


@app.route("/")
def index():
    return render_template("index.html")

##################
# USER STUFF BEGINS
##################


@app.route("/users/")
@app.route("/users/all/")
def usersAll():
    users = usersApp.getUsersAll()
    return render_template("usersAll.html", users=users)


@app.route("/users/read/")
def usersReadRender():
    return render_template("usersRead.html")


@app.route("/users/read/", methods=["POST"])
def getUserById():
    userId = request.form["userId"]
    user = usersApp.getUserById(userId)
    return render_template("usersReadFeedback.html", user=user)


@app.route("/users/create/")
def usersCreateRender():
    return render_template("usersCreate.html")


@app.route("/users/create/", methods=["POST"])
def usersCreate():
    name = request.form["name"]
    username = request.form["username"]
    email = request.form["email"]
    user = {
        "name": name,
        "username": username,
        "email": email
    }
    usersApp.userCreate(user)
    return render_template("usersCreatedFeedback.html", user=user)


@app.route("/users/update")
def usersUpdateRender():
    return render_template("usersUpdate.html")


@app.route("/users/update/", methods=["POST"])
def usersUpdate():
    userId = request.form["id"]
    name = request.form["name"]
    username = request.form["username"]
    email = request.form["email"]
    user = {
        "id": userId,
        "name": name,
        "username": username,
        "email": email
    }
    usersApp.userUpdate(user)
    return render_template("usersUpdatedFeeback.html", user=user)

@app.route("/users/delete")
def usersDeleteRender():
    return render_template("usersDelete.html")

@app.route("/users/delete/", methods=["POST"])
def usersDelete():
    userId = request.form["id"]
    user = usersApp.getUserById(userId)
    usersApp.userUpdate(user)
    return render_template("usersDeletedFeedback.html", user=user)

##################
# USER STUFF ENDS
##################

##################
# TASK STUFF BEGINS
##################


@app.route("/todos/")
def todosAll():
    todos = todosApp.getTodosAll()
    return render_template("todosAll.html", todos=todos)


@app.route("/todos/read/")
def todosReadRender():
    return render_template("todosRead.html")


@app.route("/todos/read/", methods=["POST"])
def getTodoById():
    todoId = request.form["todoId"]
    todo = todosApp.getTodoById(todoId)
    return render_template("todosReadFeedback.html", todo=todo)


@app.route("/todos/create/")
def todoCreateRender():
    return render_template("todosCreate.html")


@app.route("/todos/create/", methods=["POST"])
def todosCreate():
    title = request.form["title"]
    completed = request.form["completed"]
    userId = request.form["userId"]
    todo = {
        "title": title,
        "completed": completed,
        "userId": userId
        }
    todosApp.todoCreate(todo)
    return render_template("todosCreatedFeedback.html", todo=todo)

@app.route("/todos/update/")
def todosUpdateRender():
    return render_template("todosUpdate.html")


@app.route("/todos/update/", methods=["POST"])
def todosUpdate():
    todoId = request.form["id"]
    title = request.form["title"]
    completed = request.form["completed"]
    todo = {
        "id": todoId,
        "title": title,
        "completed": completed,
    }
    todosApp.todoUpdate(todo)
    return render_template("todosUpdatedFeeback.html", todo=todo)

@app.route("/todos/delete")
def todosDeleteRender():
    return render_template("todosDelete.html")

@app.route("/todos/delete/", methods=["POST"])
def todosDelete():
    todoId = request.form["id"]
    todo = todosApp.getTodoById(todoId)
    todosApp.todoDelete(todo)
    return render_template("todosDeletedFeedback.html", todo=todo)

##################
# USER STUFF ENDS
##################


if __name__ == "__main__":
    app.run(debug=True, port=5001)
