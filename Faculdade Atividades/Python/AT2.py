def contar_digitos(numero):
    numero_str = str(numero)
    quantidade_digitos = len(numero_str)
    return quantidade_digitos

numero = int(input("Digite um Numero"))
quantidade = contar_digitos(numero)
print(f"O número {numero} tem {quantidade} dígitos.")

