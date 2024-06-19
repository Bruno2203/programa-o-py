print("Objetivo:")
objetivo = "Magnos tem como objetivo passar por todos 4 mundos do reino mistíco, e chegando em Asgard passar por todos seus desafios e se tornar Magnos o Feiticeiro supremo!"
print(objetivo)

def pausar(palavra):
    entrada = ""
    while entrada != palavra:
        entrada = input("Digite 's' para dar continuidade: ")
        if entrada != palavra:
            print("Palavra incorreta. Tente novamente.")
    print("Palavra confirmada, autorização conedida")

pausar("s")
print("O programa foi retomado.")

import csv

vetor = []
with open('projeto.csv', 'r') as arquivo_csv:
    reader =  csv.DictReader(arquivo_csv)
    for row in reader:
        vetor.append(row)

def imprimir_aventura(nome_arquivo, nome_coluna):
    for linha in reader:
        print(linha[nome_coluna])







def escolher_e_imprimir(nome_arquivo, nome_coluna):
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        if nome_coluna not in leitor_csv.fieldnames:
            print(f"Coluna '{nome_coluna}' não encontrada no arquivo CSV.")
            return

        elementos_coluna = [linha[nome_coluna] for linha in leitor_csv]

        print("Escolha um número correspondente ao elemento que deseja imprimir:")
        for i, elemento in enumerate(elementos_coluna):
            print(f"{i+1}: {elemento}")

        escolha = int(input("Digite o número correspondente: "))
        if 1 <= escolha <= len(elementos_coluna):
            print(f"O elemento correspondente ao número {escolha} é: {elementos_coluna[escolha-1]}")
        else:
            print("Número inválido!")





def remover_elemento(nome_arquivo, nome_coluna):
    linhas = []
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        if nome_coluna not in leitor_csv.fieldnames:
            print(f"Coluna '{nome_coluna}' não encontrada no arquivo CSV.")
            return
        for linha in leitor_csv:
            linhas.append(linha)
    elementos_coluna = [linha[nome_coluna] for linha in linhas]
    elementos_coluna = elementos_coluna[:40] + elementos_coluna[44:]
    print("Escolha um número correspondente ao elemento que deseja remover:")
    for i, elemento in enumerate(elementos_coluna):
        print(f"{i+1}: {elemento}")
    escolha = int(input("Digite o número correspondente: "))
    if not (1 <= escolha <= len(elementos_coluna)):
        print("Número de aventura inválido!")
        return
    # Remove o elemento da lista
    elemento_removido = elementos_coluna.pop(escolha - 1)
    # Atualiza o arquivo CSV com a lista modificada
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=leitor_csv.fieldnames)
        escritor_csv.writeheader()
        for linha in linhas:
            if linha[nome_coluna] != elemento_removido:
                escritor_csv.writerow(linha)
    print(f"A aventura '{elemento_removido}' foi removida com sucesso.")

nome_arquivo = 'projeto.csv'
nome_coluna = 'Aventuras:'

imprimir_aventura(nome_arquivo, nome_coluna)

