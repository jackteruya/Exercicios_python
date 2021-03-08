import pandas as pd

from io import StringIO



#df = pd.read_csv("dadosAlunos.csv", usecols=['idade', 'altura']).head()

df = pd.read_csv("dadosAlunos.csv")

#print(df.to_string())

print(df[['idade', 'nome']])






'''dados['idade'].head()

print(dados)'''