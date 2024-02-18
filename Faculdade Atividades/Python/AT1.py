def number_verification(number):
    if number > 0:
        return 'P'
    else:
        return 'N'
number = int(input("Digite um número: "))
resultado = number_verification(number)
print(f"O resultado para o número {number} é: {resultado}")

