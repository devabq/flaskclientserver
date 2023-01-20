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


@app.route("/users/delete")
def usersDeleteRender():
    return render_template("usersDelete.html")

##################
# USER STUFF ENDS
##################

##################
# TASK STUFF BEGINS
##################


@app.route("/todos/")
def getTodosAll():
    todos = todosApp.getTodosAll()
    return render_template("todos.html", todos=todos)


@app.route("/todos/<int:todo_id>")
def getTodoById(todoId):
    todo = todosApp.getTodoById(todoId)(todoId)
    return render_template("todo.html", todo=todo)


@app.route("/todos/create/")
def todoCreateRender():
    return render_template("todoCreate.html")


@app.route("/todos/create/", methods=["POST"])
def todoCreate():
    title = request.form["title"]
    completed = request.form["completed"]
    userId = request.form["userId"]
    todo = {
        "title": title,
        "completed": completed,
        "userId": userid}
    todosApp.todoCreate(todo)
    return render_template("todosCreatedFeedback.html")

##################
# USER STUFF ENDS
##################


if __name__ == "__main__":
    app.run(debug=True, port=5001)
