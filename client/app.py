import requests
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


api_url = "127.0.0.1:5000"


# Listar Usuários

def listarUsuario():
    users = api_url + "/users/"
    response = requests.get(users)
    return response.json()


# Listar tarefas do usuário

def listarTarefas():
    userId = input("Você quer listar as tarefas de qual usuário?")

    lista = api_url + "/users/" + userId + "/todos/"
    responseTarefas = requests.get(lista)
    return responseTarefas.json()


# Criar/Ler/Atualizar/Deletar usuários

def criarUsuario(resultado):
    criarUsuarioUrl = api_url + "/users/"
    criar = requests.post(criarUsuarioUrl, json=resultado)
    return criar.json()


def lerUsuario(userId):
    lerUsuarioUrl = api_url + "/users/" + str(userId)
    ler = requests.get(lerUsuarioUrl)
    return ler.json()


def atualizarUsuario(userId, resultados):
    atualizarUsuarioUrl = api_url + "/users/" + str(userId)
    atualizar = requests.put(atualizarUsuarioUrl, json=resultados)
    return atualizar.json()


def deletarUsuario(userId):
    deletarUsuarioUrl = api_url + "/users/" + str(userId)
    deletar = requests.delete(deletarUsuarioUrl)
    return deletar.json()

# CRUD CLI


tarefasUrl = api_url + "/todos/"


def ctarefas(tarefas1):
    criarTarefas = requests.post(tarefasUrl, json=tarefas1)
    return criarTarefas.json()


def ltarefas(tarefasId):
    lerTarefasUrl = tarefasId + str(utarefasId)
    lertarefas = requests.get(lerTarefasUrl)
    return lertarefas.json()


def atarefas(tarefasId, tarefas1):
    atualizarTarefasUrl = tarefasUrl = str(tarefasId)
    atualizarTarefas = requests.put(atualizarTarefasUrl, json=tarefas1)
    return atualizarTarefas.json()


def dtarefas(tarefasId):
    deletarTarefasUrl = tarefasUrl = str(tarefasId)
    deletarTarefas = requests.delete(deletarTarefasUrl)
    return deletarTarefas.json()
