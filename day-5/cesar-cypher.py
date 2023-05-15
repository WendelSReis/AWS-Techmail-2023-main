"""
Cesar Cypher
"""

# funcao para duplicar o alfabeto
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


# funcao para solicitar a mensagem a ser encriptada
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt


# numero de chave para encriptar
# numero entre 1 e 25
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount


# funcao para encriptar a mensagem
def encryptMessage(message, cipherKey, alphabet):
    # iniciando variaveis
    encryptedMessage = ""
    uppercaseMessage = ""
    
    # convertendo mensagem para letras maiusculas
    uppercaseMessage = message.upper()
    
    # loop
    for currentCharacter in uppercaseMessage:
        
        # percorrendo as letras do alfabeto
        position = alphabet.find(currentCharacter) # ABCDEFG # A = 0, B = 1, C = 2
        
        # gerando nova posicao a partir da chave de cifra
        newPosition = position + int(cipherKey) # A = 0 CHAVE = 5 => 0 + 5 
        
        # condicional
        # se a letra contem no alfabeto
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition] # B = 1, CHAVE = 5 => 5 + 1 = 6 => G
        else:
            encryptedMessage = encryptedMessage + currentCharacter
            
    # retorna a mensagem encriptada
    return encryptedMessage



# decriptar a mensagem
def decryptMessage(message, cipherKey, alphabet):
    
    # retornar a posicao original
    decryptKey = -1 * int(cipherKey)
    
    # retornar a mensagem decriptada
    return encryptMessage(message, decryptKey, alphabet)
    

# funcao principal do programa de cifras
def runCaesarCipherProgram():
    # definicao do alfabeto
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    
    # chamando a funcao para duplicar o alfabeto
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    # recuperar mensagem do usuario
    myMessage = getMessage()
    print(myMessage)
    
    # recuperar a chave de cifra
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    # encriptar a mensagem
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    # decriptar a mensagem
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    

# executando a funcao principal
runCaesarCipherProgram()

