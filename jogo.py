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

# Exemplo de uso
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

# Exemplo de uso
nome_arquivo = 'projeto.csv'
nome_coluna = 'Aventuras:'
imprimir(nome_arquivo, nome_coluna)


def escrever_aventura(nome_arquivo, aventura_1):
    linhas = []
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabecalho = next(leitor_csv)
        if nome_coluna not in cabecalho:
            print(f"Coluna '{nome_coluna}' não encontrada no arquivo CSV.")
            return
        for linha in leitor_csv:
            linhas.append(linha)
        i = cabecalho.index(nome_coluna)
        for linha in linhas:
            linha.insert(i, '')
            linha[i] = aventura_1

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(linhas)
        print("Nova aventura adicionada com sucesso!")


aventura_1 = input("Digite a nova aventura: ")
escrever_aventura(nome_arquivo, aventura_1)
imprimir(nome_arquivo, nome_coluna)





#remove aventura
def remove_aventura(nome_arquivo, aventura):
    linhas_modificadas = []

    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        cabecalho = leitor.fieldnames

        for linha in csv:
            if linha['AVENTURA:'] != aventura:
                linhas_modificadas.remove(linha)

    print(f"Aventura '{aventura}' removida com sucesso do arquivo CSV.")

# Exemplo de uso
nome_arquivo = 'projeto.csv'
aventura = 'Aventura 1'
remove_aventura(nome_arquivo, aventura)
