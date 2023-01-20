import requests

class Users:
    apiUrl = "http://localhost:5000/users/"

    def getUsersAll(self):
        return requests.get(self.apiUrl).json()

    def getUserById(self, userId):
        return requests.get(f"{self.apiUrl}/{userId}").json()

    def userCreate(self, user):
        return requests.post(self.apiUrl, json=user).json()

    def userUpdate(self, user):
        return "USER UPDATED", 200
    
    def userDelete(self, userId):
        return "USER DELETED", 200