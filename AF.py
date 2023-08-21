import time
import timeit


class AF:
    def __init__(self, inicial, final, transitions, path): #construtor eh o q instancia a classe e inicializa os atributos
        print("AFD")
        self.inicial = inicial #self eh o proprio objeto(atributo)
        self.final = final
        self.transitions = transitions
        self.lista_input = self.lerEntrada(path)

    def lerEntrada(self, path): #metodo
        arq = open(path, 'r')
        input = arq.readlines()
        #tirando os \n
        for i in range(len(input)):
            input[i] = input[i].replace('\n', '')
        arq.close()
        return input

    def verificarCondicao(self, output):
        #começo do tempo de execução
        tempo_inicial = timeit.default_timer()

        for linha in self.lista_input:
            #inicializar o estado atual com o estado inicial
            estado_atual = self.inicial
            #para cada caracter da linha
            for caracter in linha:
                if caracter == ";":
                    break
                for j in self.transitions:
                    if j["from"] == estado_atual:
                        if j["read"] == caracter:
                            estado_atual = j["to"]                   
                            break
                else:
                    estado_atual = "erro"
                    break
            if estado_atual in self.final:
                #Tempo final de execução
                tempo_final = timeit.default_timer()-tempo_inicial
                output.write(linha + ";1;"+str(round(tempo_final,5))+"\n")
            else:
                #Tempo final de execução
                tempo_final = timeit.default_timer()-tempo_inicial
                output.write(linha + ";0;"+str(round(tempo_final,5))+"\n")
        output.close()

