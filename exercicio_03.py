"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

paisA: int = 80000
taxaA: float = 3
paisB: int = 200000
taxaB: float = 1.5

tempo = 0

while paisA < paisB:
    paisA: int = paisA * ((1 + taxaA/100) ** 1)
    paisB: int = paisB * ((1 + taxaB/100) ** 1)
    print(int(paisA), " ", int(paisB))
    tempo += 1


print("População do país A {} e do país B {}.".format(int(paisA), int(paisB)))
print("São necessários {} anos.".format(tempo))
