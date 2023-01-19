import requests


class Users:
    apiUrl = "http://localhost:5000/users"

    def getUsersAll(self):
        return requests.get(self.apiUrl).json()

    def getUsersId(self, userId):
        return requests.get(f"{self.apiUrl}/{userId}").json()

    def usersCreate(self, user):
        return requests.post(self.apiUrl, json=user).json()
