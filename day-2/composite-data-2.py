"""
Working with Composite Data Types
"""

# o uso de imports
import csv # lib que trabalha com arquivos csv
import copy # lib que trabalha com copia de dados

# definir nosso dicionario modelo
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# loop de repeticao
# laço

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

    
"""
vin : <empty>
make : <empty>
model : <empty>
year : 0
range : 0
topSpeed : 0
zeroSixty : 0.0
mileage : 0
"""

# criar nova lista vazia
myInventoryList = []

# manipular o arquivo CSV
with open('day-2/car_fleet.csv') as csvFile:
    # leitura do arquivo
    # salvar em memoria
    csvReader = csv.reader(csvFile, delimiter=',')
    
    # variavel de controle
    lineCount = 0
    
    # iterar sobre o arquivo
    for row in csvReader:
        # imprimir o cabeçalho // nome das colunas
        # condicional
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            # incrementar a variavel de controle
            lineCount += 1
        else:
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}') 
            # copia duplicada
            currentVehicle = copy.deepcopy(myVehicle)
            # popular o dicionario com os dados vindo do CSV
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7] 
            # adicionar o dado populado
            myInventoryList.append(currentVehicle)
            # incrementar a variavel de controle
            lineCount += 1
        # mostrar contagem das linhas
        print(f'Processed {lineCount} lines.')
        
    
    """
    vin : <empty>
    make : <empty>
    model : <empty>
    year : 0
    range : 0
    topSpeed : 0
    zeroSixty : 0.0
    mileage : 0
    Column names are: vin, make, model, year, range, topSpeed, zeroSixty, mileage
    Processed 1 lines.
    vin: TMX20122, make: AnyCompany Motors, model:  Coupe, year:  2012, range:  335, topSpeed:  155, zeroSixty:  4.1, mileage:  50000
    Processed 2 lines.
    vin: TM320163, make: AnyCompany Motors, model:  Sedan, year:  2016, range:  240, topSpeed:  140, zeroSixty:  5.2, mileage:  20000
    Processed 3 lines.
    vin: TMX20121, make: AnyCompany Motors, model:  SUV, year:  2012, range:  295, topSpeed:  155, zeroSixty:  4.7, mileage:  100000
    Processed 4 lines.
    vin: TMX20204, make: AnyCompany Motors, model:  Truck, year:  2020, range:  300, topSpeed:  155, zeroSixty:  3.5, mileage:  0
    Processed 5 lines.
    """
    
    # exibir os dados do inventario
    # estrutura de repeticao
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
        print("-----------------\r")
        


"""
vin : TMX20204
make : AnyCompany Motors
model :  Truck
year :  2020
range :  300
topSpeed :  155
zeroSixty :  3.5
mileage :  0
-----------------
"""