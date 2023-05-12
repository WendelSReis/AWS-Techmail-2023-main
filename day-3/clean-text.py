# importar uma biblioteca
import re
import os

# ler o arquivo
with open('day-3/preproinsulin-seq.txt') as f:
    insulinFile = f.read()

# exibir os dados do arquivo
print("----- DADO ORIGINAL -----")
print(insulinFile)

"""
----- DADO ORIGINAL -----
ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
"""

# limpar os dados
# funcao
def clean_text(string):
    # remover ORIGIN
    string = string.replace("ORIGIN", "")
    # REGEX remover os numeros
    string = re.sub(r"\d+", "", string)
    # remover o 61
    #string = string.replace("61", "")
    # remover o 1
    #string = string.replace("1", "")
    # remover o //
    string = string.replace("//", "")
    #remover os espacos em branco
    #string = string.replace(" ", "")
    # REGEX remover os espacos em branco
    string = re.sub(r"\s", "", string)
    # remover a quebra de linha
    string = string.replace("\n", "")
    
    # retornar a string formatada
    return string

# dado limpo
cleanInsulin = clean_text(insulinFile)

# exibir os dados do arquivo limpo
print("----- DADO LIMPO -----")
print(cleanInsulin)

with open('day-3/preproinsulin-seq.txt') as f:
    insulinFile = f.read()


"""
----- DADO LIMPO -----
      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
"""


"""
----- DADO LIMPO -----
malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn
"""

# contagem de caracteres
print("----- CONTAGEM DE CARACTERES -----")
print("Quantidade de caracteres: {}".format(len(cleanInsulin)))

"""
----- CONTAGEM DE CARACTERES -----
Quantidade de caracteres: 110
"""

# classificar os dados
print('----- DADOS CLASSIFICADOS')

# LS
print(f'EXEMPLO LS: {cleanInsulin[0:24]}')

# atribuindo valores dinamicamente
lsInsulin = cleanInsulin[0:24]
bInsulin = cleanInsulin[25:35]
aInsulin = cleanInsulin[36:50]
cInsulin = cleanInsulin[21:110]

# contagem
print(f"Contagem LS: { len(lsInsulin) }")

# criar arquivos

# print(os.)

names = ["lsInsulin", "bInsulin", "aInsulin", "cInsulin"]

for insulin in names:
    fw = open('day-3/' + str(insulin).upper() + "-seq-clean", "w")
    fw.write(globals()[insulin])
    fw.close()

"""
----- DADOS CLASSIFICADOS
LS: malwmrllpllallalwgpdpaaa
"""



