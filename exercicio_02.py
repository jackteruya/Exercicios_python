"""
Faça um programa que leia e valide as seguintes informações:
  a.Nome: maior que 3 caracteres;
  b.Idade: entre 0 e 150;
  c.Salário: maior que zero;
  d.Sexo: 'f' ou 'm';
  e.Estado Civil: 's', 'c', 'v', 'd';

O programa só deve terminar, mostrando a mensagem de ‘dados lidos com sucesso’,
quando todos os dados forem informados corretamente.
"""

nome = str(input("Digite o nome: "))
contadorNome = len(nome)
while contadorNome <= 3:
    contadorNome = 0
    nome = str(input("Não é possivel nome menor que 3 caracteres!" 
                     "Digite novamente o nome: "))
    contadorNome = len(nome)

idade = int(input("Digite a idade: "))
while (idade < 0) or (idade > 150):
    idade = int(input("Digite a idade: "))

salario = int(input("Digite o salário: "))
while salario <= 0:
    print("Valor invalido!")
    salario = int(input("Digite novamente o salário: "))

sexo = str(input("Digite o Sexo[f/m]: ")).strip().lower()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados Invalidos! Digite o Sexo[f/m]: ")).strip().lower()[0]

estadoCivil = str(input("Digite o Estado Civil[s / c / v / d]: ")).strip().lower()[0]
while estadoCivil not in 'SsCcVvDd':
    estadoCivil = str(input("Dados Invalidos! Digite o Estado Civil[s / c / v / d]: ")).strip().lower()[0]

print("\nDados lidos com sucesso")
