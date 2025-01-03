# Solicitar como entrada dois números e depois
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Solicitar a operação  matemática que deseja realizar
operacao = input("Digite a operação matemática que deseja realizar (+, -, *, /): ")

# Realizar a operação matemática
if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(abs(num1 - num2))
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)
else:
    print("Operação inválida")

