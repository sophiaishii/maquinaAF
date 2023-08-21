import json

from AF import AF
from AFND import AFND
from AFE import AFE

if __name__ == "__main__":
    # path = "det/entrada.txt"
    # with open("det/automato.json", "r") as f:
    #     data = json.load(f)
    # #Cria o arquivo output
    # output = open("det/output.txt", "w")
    # maquina = AF(data["inicial"], data["final"], data["transitions"], path)
    # maquina.verificarCondicao(output)
    
    path = "ndet/ex2_input.txt"
    with open("ndet/automato.json", "r") as f:
        data = json.load(f)
    #Cria o arquivo output
    output = open("ndet/output.txt", "w")
    maquina = AFND(data["inicial"], data["final"], data["transitions"], path)
    maquina.verificarCondicao(output)

    # path = "mvazio/entrada.txt"
    # with open("mvazio/automato.json", "r") as f:
    #    data = json.load(f)
    # cria o arquivo output
    # output = open("mvazio/output.txt", "w")
    # maquina = AFE(data["inicial"], data["final"], data["transitions"], path)
    maquina.verificarCondicao(output)
