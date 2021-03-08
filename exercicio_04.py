cadastroPessoa = []

while len(cadastroPessoa) < 2:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    altura = int(input("Altura (cm): "))
    print("\n")
    if idade < 18:
        cadastroPessoa.append({'Nome': nome, 'Idade': idade,
                               'Altura': altura, 'Observação': 'Menor de idade'})
    else:
        cadastroPessoa.append({'Nome': nome, 'Idade': idade, 'Altura': altura, })

listaOrdemIdade = sorted(cadastroPessoa, key=lambda key: key['Idade'])

for x in listaOrdemIdade:
    for y in x:
        print(y, ":", x[y])
    print('\n')
