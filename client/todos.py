import requests
class Todos:
    apiUrl = "http://localhost:5000/todos"

    def get_todos(self):
        return requests.get(self.apiUrl).json()

    def get_todo_by_id(self, todo_id):
        return requests.get(f"{self.apiUrl}/{todo_id}").json()

    def todoCreate(self, todo):
        return requests.post(self.apiUrl, json=todo).json()
