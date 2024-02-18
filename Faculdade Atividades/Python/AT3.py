def somar(numero1, numero2 ):
    Resultado = numero1 + numero2
    print ("O resultado da soma é", Resultado)

def subtrair(numero1, numero2):
    Resultado = numero1 - numero2
    print ("O resultado da subtração é", Resultado)

def dividir(numero1, numero2):
    if numero2 == 0:
        print("Não é possível dividir por zero!")
    else:
        resultado = numero1 / numero2
        print("O resultado da divisão é", resultado)

def multiplicar(numero1, numero2):
    Resultado = numero1 * numero2
    print ("O resultado da multiplicação é", Resultado)


numero1 =float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))
operation = (input("Escolha qual a operação (somar, subtrair, dividir, multiplicar): "))
if operation == 'somar':
    somar(numero1, numero2)
elif operation == 'subtrair':
    subtrair(numero1, numero2)
elif operation == 'dividir':
    dividir(numero1, numero2)
elif operation == 'multiplicar':
    multiplicar(numero1, numero2)