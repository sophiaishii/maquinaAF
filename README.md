## **RELATÓRIO DE DESENVOLVIMENTO DO TRABALHO DE AUTÔMATOS FINITOS DA MATÉRIA DE TEORIA DA COMPUTAÇÃO** <h2>


### Nesse simulador, desenvolvemos as seguintes máquinas: <h3>
* Autômato Finito Determinístico (AF);
* Autômato Finito Não Determinístico (AFND);
* Autômato Finito com Movimentos Vazios (AFE);

### Funcionamento: <h3>
  O trabalho foi desenvolvido em python orientado a objeto. Primeiro ele lê o arquivo automato.json e depois recebe o arquivo input.txt para reconhecer as entradas. No final, ele gera um arquivo output.txt que informa a palavra de entrada, o resultado esperado, se as entradas foram aceitas ou rejeitadas e o tempo de processamento.

### Processamento: <h3>
  O método **lerEntrada** lê as linhas do arquivo de entrada e o método **verificarCondicao** é usado para verificar cada entrada da lista. Ele verifica, para cada caractere, as transições do autômato para determinar o próximo estado e, se o caractere não conseguir ser lido por essas transições, o autômato entra em um estado de erro. Se o estado estiver na lista de estados finais, a entrada é considerada aceita e é registrada em um arquivo de saída com valor 1, mas caso contrário, será rejeitada e o seu valor será 0. O tempo de execução para processar cada entrada é medido usando a biblioteca **timeit** e é registrado no arquivo de saída.

### AFD <h3>
**automato.json**
```
{
    "inicial": 0,
    "final": [2],
    "transitions": [
        {"from": 0,"read": "b", "to": 1}, 
        {"from": 0,"read": "a", "to": 0},
        {"from": 1,"read": "a", "to": 2},
        {"from": 2,"read": "a", "to": 2},
        {"from": 1,"read": "b", "to": 1}
    ]
}
```

**input.txt**
```
ba;1
aaaabbbbbaaaaa;1
abababab;0
bbbbbbbb;0
aaaaaaaaaaaa;0
aaaaabaaaaa;1
```

**output.txt**
```
ba;1;1;0.00027
aaaabbbbbaaaaa;1;1;0.00041
abababab;0;0;0.00054
bbbbbbbb;0;0;0.00075
aaaaaaaaaaaa;0;0;0.00103
aaaaabaaaaa;1;1;0.00127
```

### AFND <h3>
**automato.json**
```
{
    "inicial": 0,
    "final": [3],
    "transitions": [
        {"from": 0,"read": "a", "to": 0}, 
        {"from": 0,"read": "b", "to": 0},
        {"from": 0,"read": "c", "to": 1},
        {"from": 0,"read": "c", "to": 0},
        {"from": 1,"read": "a", "to": 2},
        {"from": 2,"read": "b", "to": 3}
    ]
}
```

**input.txt**
```
acab;1
bcab;1
ccab;1
abccab;1
abcba;0
cbab;0
bcac;0
```

**output.txt**
```
acab;1;1;0.00131
bcab;1;1;0.00206
ccab;1;1;0.00283
abccab;1;1;0.00413
abcba;0;0;0.00672
cbab;0;0;0.00709
bcac;0;0;0.00756
```

### AFE <h3>
**automato.json**
```
{
    "inicial": 0,
    "final": [3],
    "transitions": [
        {"from": 0,"read": "a", "to": 0}, 
        {"from": 0,"read": "b", "to": 0},
        {"from": 0,"read": "c", "to": 1},
        {"from": 0,"read": "ε", "to": 0},
        {"from": 0,"read": "c", "to": 0},
        {"from": 1,"read": "a", "to": 2},
        {"from": 2,"read": "b", "to": 3}
    ]
}
```

**input.txt**
```
εba;1
εaaaabbbbbaaaaa;1
```

**output.txt**
```
εba;1;1;0.00042
εaaaabbbbbaaaaa;1;1;0.00073
```
