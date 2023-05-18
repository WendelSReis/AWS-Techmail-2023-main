"""
Utilizando o modulo OS
"""

# importar o modulo
import os
import subprocess

# retornar a listagem da pasta
# utilizando o .system()
print("----- OS SYSTEM ------")
os.system("ls")

print("----- SUBPROCESS ------")
# utilizando o subprocess
subprocess.run(["ls"])

# retornar arquivos e pastas com infos
print("----- DETALHES ------")
subprocess.run(["ls","-l"])

# retornar informacao de arquivo especifico
print("----- ESPECIFICO ------")
subprocess.run(["ls","-l","README.md"])


# executar comando armazenados em variaveis
"""
# variaveis
command="uname"
commandArgument="-a"

# mensagem informativa
print(f'Gathering system information with command: {command} {commandArgument}')

# executar
subprocess.run([command,commandArgument])
"""

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

