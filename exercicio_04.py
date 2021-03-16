cadastroPessoa = []

while len(cadastroPessoa) < 5:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    altura = int(input("Altura (cm): "))
    print("\n")
    cadastroPessoa.append({'Nome': nome, 'Idade': idade, 'Altura': altura})
    if idade < 18:
        cadastroPessoa[-1]['Observação'] = 'Menor de idade'

listaOrdemIdade = sorted(cadastroPessoa, key=lambda key: key['Idade'])

for x in listaOrdemIdade:
    for y in x:
        print(y, ":", x[y])
    print('\n')
