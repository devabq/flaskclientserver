from flask import Flask, request, render_template
import users
import todos

app = Flask(__name__)

usersApp = users.Users()
todosApp = todos.Todos()


@app.route("/")
def index():
    return render_template("index.html", users=users)


@app.route("/users/all")
def usersAll():
    users = usersApp.getUsersAll()
    return render_template("usersAll.html", users=users)


@app.route("/users/create")
def usersCreateRender():
    return render_template("usersCreate.html")


@app.route("/users/create", methods=["post"])
def usersCreate():
    name = request.form["name"]
    username = request.form["username"]
    email = request.form["email"]
    user = {
        "name": name,
        "username": username,
        "email": email
    }
    usersApp.usersCreate(user)
    return render_template("usersCreatedFeedback.html")


@app.route("/users/read")
def usersReadRender():
    return render_template("usersRead.html")


@app.route("/users/<int:userId>")
def getUsersId(userId):
    user = usersApp.getUsersId(userId)
    return render_template("usersReadFeedback.html", user=user)


@app.route("/users/update")
def usersUpdateRender():
    return render_template("usersUpdate.html")


@app.route("/users/delete")
def usersDeleteRender():
    return render_template("usersDelete.html")


@app.route("/todos")
def get_todos():
    todos = todosApp.get_todos()
    return render_template("todos.html", todos=todos)


@app.route("/todos/<int:todo_id>")
def get_todo_by_id(todo_id):
    todo = todosApp.get_todo_by_id(todo_id)
    return render_template("todo.html", todo=todo)


@app.route("/todos/new")
def new_todo():
    return render_template("todoCreate.html")


@app.route("/todos", methods=["POST"])
def todoCreate():
    title = request.form["title"]
    completed = request.form["completed"]
    user_id = request.form["user_id"]
    todo = {
        "title": title,
        "completed": completed,
        "userId": user_id
    }
    todosApp.todoCreate(todo)
    return "Tarefa criada"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
