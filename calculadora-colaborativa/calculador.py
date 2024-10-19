
# Função de soma
def somar(num1, num2):
    return num1 + num2

# Função de subtração
def subtracao(num1, num2):
    return num1 - num2

# Função de multiplicação
def multiplicacao(num1, num2):
    return num1 * num2

# Função de divisão
def divisao(num1, num2):
    return num1 / num2  # A validação de divisão por zero será feita na função de validação


# Função para validar a entrada
def validar_entrada(num1, num2, operacao):
    if operacao not in ["+", "-", "*", "/", "**", "sqrt"]:
        print("Operação inválida.")
        return False
    if operacao == "/" and num2 == 0:
        print("Divisão por zero não permitida.")
        return False
    return True

# Função principal da calculadora
def calculadora():
    historico = []
    operacoes = {
        "+": somar,
        "-": subtracao,
        "*": multiplicacao,
        "/": divisao,
    }

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /, **, sqrt): ")

            # Validação de entrada
            if not validar_entrada(num1, num2, operacao):
                continue

            # Execução da operação
            resultado = operacoes[operacao](num1, num2)
            historico.append(f"{num1} {operacao} {num2} = {resultado}")
            print("Resultado:", resultado)
            print("Histórico:", historico)
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
        except KeyError:
            print("Operação inválida.")

        # Pergunta se o usuário quer continuar
        continuar = input("Deseja fazer outra operação? (s/n): ")
        if continuar.lower() != 's':
            break

calculadora()
