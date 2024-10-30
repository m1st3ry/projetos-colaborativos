# Função de conversão
def converter(real, dolar):
    resultado = real / dolar  # Divide para obter o valor convertido em reais
    
    return resultado

# Definindo o valor em reais e a taxa de conversão do dólar
real = float(input("Digite o valor em reais: "))
dolar = float(input("Digite a taxa de conversão do dólar: "))

# Chamando a função de conversão
valor_convertido = converter(real, dolar)

# Informando os valores convertidos
print(f"O valor em dólares que você vai ter é: {valor_convertido:.2f} dólares")
