def calcular(numero1, numero2, operacao):
    if operacao == 'somar':
        resultado = numero1 + numero2
    elif operacao == 'subtrair':
        resultado = numero1 - numero2
    elif operacao == 'dividir':
        if numero2 == 0:
            return "Não é possível dividir por zero!"
        resultado = numero1 / numero2
    elif operacao == 'multiplicar':
        resultado = numero1 * numero2
    else:
        return "Operação inválida"
    
    return resultado

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
operacao = input("Escolha qual a operação (somar, subtrair, dividir, multiplicar): ")

resultado = calcular(numero1, numero2, operacao)

if (resultado) == str:
    print(resultado)
else:
    print("O resultado da operação é:", resultado)
