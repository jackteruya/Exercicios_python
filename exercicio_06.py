import pandas as pd

localArquivo = input("Digite o local do arquivo: ")

df = pd.read_csv(localArquivo, dtype={"nome": str, "idade": int, "altura": int})

qtdeAluno = len(df['nome'])

print("Quantidade de alunos: {}".format(qtdeAluno))

mediaAltura = float(df['altura'].sum()/qtdeAluno)

print("Altura média dos alunos: {:.2f}".format(mediaAltura))

alturaMaiorMedia = 0
idadeMaior13 = 0

df2 = df.loc[(df['altura']<mediaAltura) & (df['idade']>13)]


print("Total de alunos com mais de 13 anos e altura inferior" +
      " a média de altura dos alunos: {}\n".format(len(df2)))

print(df2)
