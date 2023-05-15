"""
Read Json Module
"""

# importando o modulo JSON
import json

# funcao com tratamento de excecao
def readJsonFile(fileName):
    data = ""
    
    # estrutura de tratamento de excecao
    try:
        # leitura do arquivo json
        with open(fileName) as json_file:
            data = json.load(json_file)
            
    # caso ocorra algum erro de leitura
    except IOError:
        print("Could not read file")

    # retorna o conteudo do arquivo
    return data


# file = readJsonFile('day-5/insulin.json')
# print('JSON: {}'.format(file))

