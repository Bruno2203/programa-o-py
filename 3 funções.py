print("Objetivo:")
objetivo = "Magnos tem como objetivo passar por todos 4 mundos do reino mistíco, e chegando em Asgard passar por todos seus desafios e se tornar Magnos o Feiticeiro supremo!"
print(objetivo)

def pausar(palavra):
    entrada = ""
    while entrada != palavra:
        entrada = input("Digite 'entendi' para dar continuidade: ")
        if entrada != palavra:
            print("Palavra incorreta. Tente novamente.")
    print("Palavra confirmada, autorização conedida")

pausar("entendi")
print("O programa foi retomado.")



import csv

def imprimir(nome_arquivo, nome_coluna):
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        if nome_coluna not in leitor_csv.fieldnames:
            print(f"Coluna '{nome_coluna}' não encontrada no arquivo CSV.")
            return

        for linha in leitor_csv:
            print(linha[nome_coluna])


nome_arquivo = 'projeto.csv'
nome_coluna = 'Aventuras:'
imprimir(nome_arquivo, nome_coluna)




def escolher_e_imprimir(nome_arquivo, nome_coluna):
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        if nome_coluna not in leitor_csv.fieldnames:
            print(f"Coluna '{nome_coluna}' não encontrada no arquivo CSV.")
            return

        elementos_coluna = [linha[nome_coluna] for linha in leitor_csv]
        elementos_coluna = elementos_coluna[:40] + elementos_coluna[44:]

        print("Escolha um número correspondente ao elemento que deseja imprimir:")
        for i, elemento in enumerate(elementos_coluna):
            print(f"{i+1}: {elemento}")

        escolha = int(input("Digite o número correspondente à aventura que deseja repetir: "))
        if 1 <= escolha <= len(elementos_coluna):
            print(f"O elemento correspondente ao número {escolha} é: {elementos_coluna[escolha-1]}")
        else:
            print("Número inválido!")







nome_arquivo = 'projeto.csv'
nome_coluna = 'Aventuras:'

escolher_e_imprimir(nome_arquivo, nome_coluna)


