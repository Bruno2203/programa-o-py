import csv

with open("projeto-rpg.xlsx", "r") as arquivo:
    arquiv_csv = csv.reader(arquivo, delimiter = ",")
    for i, linha in enumerate(arquiv_csv):
        if i == 0:
            print("cabeçalho: " + str(linha))
        else:
            print("valor: " + str(linha))