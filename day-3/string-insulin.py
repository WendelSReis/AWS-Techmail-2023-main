# Store the human preproinsulin sequence in a variable called preproinsulin:


preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# concatenacao de variaveis
insulin = bInsulin + aInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:
print(preproInsulin)

"""
malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn
"""

# parte A da insulina
print("The sequence of human insulin, chain a: " + aInsulin)

"""
The sequence of human insulin, chain a: giveqcctsicslyqlenycn
"""

# pesos dos aminoacidos
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Contagem de cada aminoacido  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})

# calculo das contagens dos pesos

molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())

print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

"""
The rough molecular weight of insulin: 6696.420000000001
"""

# peso atual da insulina
molecularWeightInsulinActual = 5807.63

print("Error percentage: " + 
str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))

"""
Error percentage: 15.30383306099047
"""

# dicionario
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

# contagem
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# variavel de controle
pH = 0

# loop while
while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    
    # incrementar a variavel de controle
    pH +=1
    
    print('{0:.2f}'.format(pH), netCharge)
    
"""
1.00 3.999773036108418
2.00 3.997731498980362
3.00 3.9774281495747488
4.00 3.7850011255505267
5.00 2.540057926152534
6.00 0.4181014741593989
7.00 -0.9698633190556047
8.00 -2.186629624776233
9.00 -4.403272105402016
10.00 -7.551924685030059
11.00 -9.980672054414311
12.00 -12.349327503864025
13.00 -13.168625084165932
14.00 -13.75988990979344
15.00 -13.969868023471733
"""
    