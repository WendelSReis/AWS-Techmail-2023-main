"""
Listar numeros primos
"""

# listar os numeros primos de 1 a 250
numerosPrimos = []

# estrutura de repeticao
for i in range(1, 251):
# verificar se o numero eh primo
# numero primo sao aqueles que apresentam dois divisores
# um e o proprio numero
    #print(i)
    
    # verificar se eh divisivel
    # condicional
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break # finaliza a execucao
        else:
            #print(i)
            numerosPrimos.insert(0, i)

# criar o arquivo    
file = "day-7/numbers.txt"

# escrever no arquivo
with open(file, "w") as f:
    numerosPrimos.reverse()
    
    # ler numero por numero
    for n in numerosPrimos:
        # inserir numeros no arquivo
        f.write(str(n) + ', ')

# ler o arquivo
with open(file, "r") as arquivo:
    print(arquivo.read())

