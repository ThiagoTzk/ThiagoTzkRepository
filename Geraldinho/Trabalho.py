resultados = [0] * 7

opcoes = [
    "0 - Encerrar entrada de dados",
    "1 - Windows XP",
    "2 - Unix",
    "3 - Linux",
    "4 - Netware",
    "5 - MacOS",
    "6 - Outro"
]

def exibir_opcoes():
    print("Opções válidas:")
    for opcao in opcoes:
        print(opcao)

while True:
    exibir_opcoes()
    resposta = int(input("Digite o número correspondente à sua resposta (0 a 6): "))

    if 0 <= resposta <= 6:
        resultados[resposta] += 1
    else:
        print("Resposta inválida. Digite um número entre 0 e 6.")

    if resposta == 0:
        break

total_respostas = sum(resultados) - resultados[0]

rotulos = [
    "Windows XP",
    "Unix",
    "Linux",
    "Netware",
    "MacOS",
    "Outro"
]

print("\nSistemas Operacionais - Votos %")
for i in range(1, 7):
    percentual = (resultados[i] / total_respostas) * 100
    print(f"{rotulos[i-1]:10} {resultados[i]} {percentual:.0f}%")

indice_vencedor = resultados.index(max(resultados[1:]))
print(f"\nO sistema operacional mais votado foi o {rotulos[indice_vencedor-1]}, "
      f"com {resultados[indice_vencedor]} votos, correspondendo a "
      f"{(resultados[indice_vencedor] / total_respostas) * 100:.0f}% dos votos.")
print(f"Total de {total_respostas} votos")