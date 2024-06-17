import csv

vetor =  []
with open('projeto.csv', 'r') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for i in leitor:
        vetor.append(i)



print(i)