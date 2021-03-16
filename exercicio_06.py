import pandas as pd
import math as m

from io import StringIO



#df = pd.read_csv("dadosAlunos.csv", usecols=['idade', 'altura']).head()

df = pd.read_csv("dadosAlunos.csv", dtype = {"nome": str, "idade": int, "altura": int})

#print(df.to_string())

#print(df[['idade', 'altura']])

altura = df[['altura']]

print(altura)



#soma = m.fsum(colunaAlutra)

#print(colunaAlutra)






'''dados['idade'].head()

print(dados)'''