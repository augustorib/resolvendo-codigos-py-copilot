# Solicitar uma string e um número inteiro como entrada. 
# Depois teremos que retornar a string repetida o número de vezes informado.

text1 = input("Digite um texto: ")
num = int(input("Digite um número de vezes que o texto irá repetir: "))

#Exibe o texto repetido com espaço entre as repetições
print((text1 + " ") * num)