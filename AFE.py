import time
import timeit


class AFE:
    def __init__(self, inicial, final, transitions, path): #construtor eh o q instancia a classe e inicializa os atributos
        print("AFE")
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
            estado_atual = [self.inicial]
            
            for caracter in linha:
                if caracter == ";":
                    break
                estado_atual_aux = []
                for estado in estado_atual:
                    for estado in estado_atual:
                # adicionar estados alcançáveis por transições regulares
                        for transicao in self.transitions:
                            if transicao["from"] == estado and transicao["read"] == caracter:
                                estado_atual_aux.extend(transicao["to"])
                        
                        # adicionar estados alcançáveis por ε-transições
                        for transicao in self.transitions:
                            if transicao["from"] == estado and transicao["read"] == "ε":
                                estado_atual_aux.extend(transicao["to"])
                    
                    estado_atual = estado_atual_aux
                    
                    if not estado_atual:
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