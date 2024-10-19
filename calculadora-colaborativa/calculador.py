def calculadora():
    """Função principal da calculadora"""

    # Solicitar os números ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Solicitar a operação   

    operacao = input("Digite a operação (+, -, *, /): ")

    # Realizar a operação
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:   

            print("Divisão por zero não é permitida.")
        else:
            resultado = num1 / num2
    else:
        print("Operação inválida.")

    # Imprimir o resultado
    print("Resultado:", resultado)

# Chamar a função principal
calculadora()