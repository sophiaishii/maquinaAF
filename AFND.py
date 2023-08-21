import time
import timeit


class AFND:
    def __init__(self, inicial, final, transitions, path): #construtor eh o q instancia a classe e inicializa os atributos
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
            estado_atual = []
            estado_atual.append(self.inicial)
            #para cada caracter da linha
            for caracter in linha:
                if caracter == ";":
                    break
                estado_atual_aux = []
                for estado in estado_atual:
                    for j in self.transitions:
                        if j["from"] == estado:
                            if j["read"] == caracter:
                                if j["to"] not in estado_atual_aux:
                                    estado_atual_aux.append(j["to"])
                                    print(estado_atual_aux, caracter)
                estado_atual = estado_atual_aux
                if estado_atual == []:
                    estado_atual = ["erro"]
                    break
                
    
                    
            print(estado_atual)
            for estado in estado_atual:
                if estado in self.final:
                #Tempo final de execução
                    tempo_final = timeit.default_timer()-tempo_inicial
                    output.write(linha + ";1;"+str(round(tempo_final,5))+"\n")
                    break
            else:
                #Tempo final de execução
                tempo_final = timeit.default_timer()-tempo_inicial
                output.write(linha + ";0;"+str(round(tempo_final,5))+"\n")
        output.close()
    
    def transicao(self, estado_atual, caracter):
        for j in self.transitions:
            if j["from"] == estado_atual:
                if j["read"] == caracter:
                    return j["to"]
        return "erro"
    
        
