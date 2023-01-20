import requests

class Todos:
    apiUrl = "http://localhost:5000/todos"

    def getTodosAll(self):
        return requests.get(self.apiUrl).json()

    def getTodoById(self, todoId):
        return requests.get(f"{self.apiUrl}/{todoId}").json()

    def todoCreate(self, todo):
        return requests.post(self.apiUrl, json=todo).json()

    def todoUpdate(self, user):
        return "TODO UPDATED", 200
    
    def todoDelete(self, userId):
        return "TODO DELETED", 200