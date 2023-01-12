from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()

import requests

api_url = "127.0.0.1:5000"



#Listar Usuários

def listarUsuario():
    users = api_url + "/users/"
    response = requests.get(users)
    return response.json()


#Listar tarefas do usuário

def listarTarefas():
    userId = input("Você quer listar as tarefas de qual usuário?")

    lista = api_url + "/users/" + userId + "/todos/"
    responseTarefas = requests.get(lista)
    return responseTarefas.json()


#Criar/Ler/Atualizar/Deletar usuários

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

#CRUD CLI

def opçoesCRUD ():
    while True:
        letra = input("Selecione CRUD:")
        if letra == "C":
            nomeUsuario = input("DIGITE SEU NOME DE USUÁRIO:")
            emailUsuario = input("DIGITE SEU EMAIL:")
            resultado =  {"name": nomeUsuario, "email": emailUsuario}
            print(criarUsuario(resultado))
        elif letra == "R":
            userId = int(input("DIGITE O ID DO USUÁRIO A SER LIDO:"))
            print(lerUsuario(userId))
        elif letra == "U":
            userId = int(input("DIGITE O ID DO USUÁRIO A SER ATUALIZADO:"))
            print(lerUsuario(userId))
            nomeUsuario = input("DIGITE SEU NOME DE USUÁRIO:")
            emailUsuario = input("DIGITE SEU EMAIL:")
            resultado =  {"name": nomeUsuario, "email": emailUsuario}
            print(atualizarUsuario(resultado,userId))
        elif letra == "D":
            userId = int(input("DIGITE O ID DO USUÁRIO A SER DELETADO:"))
            print(deletarUsuario(userId))

tarefasUrl = api_url + "/todos/"

def ctarefas (tarefas1):
    criarTarefas = requests.post(tarefasUrl, json=tarefas1)
    return criarTarefas.json()
def ltarefas (tarefasId):
    lerTarefasUrl = tarefasId + str(utarefasId)
    lertarefas = requests.get(lerTarefasUrl)
    return lertarefas.json()
def atarefas (tarefasId, tarefas1):
    atualizarTarefasUrl = tarefasUrl = str(tarefasId)
    atualizarTarefas = requests.put(atualizarTarefasUrl, json=tarefas1)
    return atualizarTarefas.json()
def dtarefas (tarefasId): 
    deletarTarefasUrl = tarefasUrl = str(tarefasId)
    deletarTarefas = requests.delete(deletarTarefasUrl)
    return deletarTarefas.json()

def opçoesCRUDtarefas():
    while True:
        letra = input("Selecione CRUD:")
        if letra == "C":
            nomeTarefa = input("DIGITE O NOME DA TAREFA:")
            descTarefas = input("DIGITE A DESCRIÇÃO DA TAREFA:")
            resultado =  {"name": nomeTarefa, "descricao": descTarefas}
            print(ctarefas(resultado))
        elif letra == "R":
            TarefasId = int(input("DIGITE O ID DA TAREFA A SER LIDA:"))
            if TarefasId > 10:
                print("Tarefa não existe")
            else:
                print(ltarefas(tarefasId))
            
        elif letra == "U":
            tarefasId = int(input("DIGITE O ID DA TAREFA A SER ATUALIZADA:"))
            nomeTarefa = input("DIGITE O NOME DA TAREFA:")
            descTarefas = input("DIGITE A DESCRIÇÃO DA TAREFA:")
            resultado =  {"name": nomeTarefa, "descricao": descTarefas}
            print(atarefas(resultado,tarefasId))
        elif letra == "D":
            tarefasId = int(input("DIGITE O ID DA TAREFA A SER DELETADA:"))
            print(dtarefas(tarefasId))