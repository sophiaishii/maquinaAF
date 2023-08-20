import json

from AF import AF

if __name__ == "__main__":
    path = "entrada.txt"
    with open("automato.json", "r") as f:
        data = json.load(f)
    #Cria o arquivo output
    output = open("output.txt", "w")
    maquina = AF(data["inicial"], data["final"], data["transitions"], path)
    maquina.verificarCondicao(output)