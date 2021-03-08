"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
  > A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  > A mensagem "Reprovado", se a média for menor do que sete;
  > A mensagem "Aprovado com Distinção", se a média for maior ou igual a dez.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

print("\n")

if media >= 10:
    print("Aprovado(a) com Distinção!")
elif media >= 7:
    print("Aprovado(a)!")
else:
    print("Reprovado(a)")
