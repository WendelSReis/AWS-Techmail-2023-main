"""
Calcular o peso da insulina JSON
"""

from jsonFileHandler import readJsonFile

data = readJsonFile('day-5/insulin.json')

print('JSON: {}'.format(data))

# verificar se os dados foram lidos
if data != "":
    # acessar posicao no arquivo json
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    
    # concatena as insulinas
    insulin = bInsulin + aInsulin
    
    # retorna peso molecular atual
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    # mostra os valores lidos
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
else:
    print("Error. Exiting program")
    

# calcular o peso molecular
aaWeights = data['weights']

# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())

pacient = data['pacient']

print("----------------------------------------------------")
print("NOME DO PACIENTE: {}".format(pacient))
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))