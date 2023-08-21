import json

from AF import AF
from AFND import AFND
from AFE import AFE

if __name__ == "__main__":
    output = open("output.txt", "w")
    with open("ndet/automato.json", "r") as f:
        data = json.load(f)
    #Confere se é AFE
    for i in data["transitions"]:
        if i["read"] == "e":
            AFE(data["inicial"], data["final"], data["transitions"], "entrada.txt").verificarCondicao(output)
            exit()
    #Confere se é AFND
    for i in data["transitions"]:
        for j in data["transitions"]:
            if i["from"] == j["from"] and i!=j:
                if i["read"] == j["read"]:
                    AFND(data["inicial"], data["final"], data["transitions"], "entrada.txt").verificarCondicao(output)
                    exit()
    else:
        AF(data["inicial"], data["final"], data["transitions"], "entrada.txt").verificarCondicao(output)
        exit()


    

    # path = "det/entrada.txt"
    # with open("det/automato.json", "r") as f:
    #     data = json.load(f)
    # #Cria o arquivo output
    # output = open("det/output.txt", "w")
    # maquina = AF(data["inicial"], data["final"], data["transitions"], path)
    # maquina.verificarCondicao(output)

    #path = "ndet/ex2_input.txt"
    #with open("ndet/automato.json", "r") as f:
    #    data = json.load(f)
    #Cria o arquivo output
    #output = open("ndet/output.txt", "w")
    #maquina = AFND(data["inicial"], data["final"], data["transitions"], path)
    #maquina.verificarCondicao(output)

    # path = "mvazio/entrada.txt"
    # with open("mvazio/automato.json", "r") as f:
    #     data = json.load(f)
    # #Cria o arquivo output
    # output = open("mvazio/output.txt", "w")
    # maquina = AFE(data["inicial"], data["final"], data["transitions"], path)
    # maquina.verificarCondicao(output)