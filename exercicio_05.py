
notas = []

nota = float(input("Nota: "))
if nota >= 0:
    notas.append(nota)

while nota > 0:
    nota = float(input("Nota: "))
    if nota >= 0:
        notas.append(nota)

# Contador de valores informados
print("\nQuantidade de valores inseridos: {}".format(len(notas)))

# Exibi todos os valores na ordem informado, uma ao lado do outro;
todasNotas = "{}".format(notas)

print("Valores informados: {}".format(todasNotas[1:-1]))

# Exibi todos os valores na ordem inversa informado, um abaixo do outro;
print("Valores na ordem inversa informado: ")
notas.reverse()
for listaInversaNotas in notas:
    print("-> ", listaInversaNotas)

# Calcula a soma dos valore informados
soma = 0
for x in notas:
    soma = soma + x
print("Soma dos valores informados: {}".format(soma))

# Calcula a média dos valores
media = soma/(len(notas))
print("Média dos valores informadods: {:.2f}".format(media))

# Calcula quantas valores acima da média e abaixo de 7
contaAcimaMedia = 0
contaAbaixoMedia = 0
for notaAcimaMedia in notas:
    if notaAcimaMedia >= 7:
        contaAcimaMedia += 1
    else:
        contaAbaixoMedia += 1

# Mostra a quantidade acima da média
print("Quantidade de valores acima da méida: {}".format(contaAcimaMedia))

# Mostra a quantidade abaixo de 7
print("Quantidade de valores abaixo de 7.00: {}".format(contaAbaixoMedia))

# Encerre o programa com uma mensagem
print("\nFim do processo! Obrigado por utilizar nossa aplicação!")
