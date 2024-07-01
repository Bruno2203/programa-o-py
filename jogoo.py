with open('Objetivo.txt', 'r') as file:
    conteudo = file.read()
print(conteudo)# Imprimindo o conteúdo lido do arquivo


# Função para pausar e continuar com base na entrada do usuário
def pausar(palavra):
    entrada = ""
    while entrada != palavra:
        entrada = input("Digite 's' para dar continuidade: ")
        if entrada != palavra:
            print("Palavra incorreta. Tente novamente.")
    print("Palavra confirmada, autorização concedida")
pausar("s")
print("O programa foi retomado.")



import csv

vetor = []
# Abrindo e lendo o arquivo CSV 'projeto.csv'
with open('projeto.csv', 'r') as arquivo_csv:
    reader =  csv.DictReader(arquivo_csv)
    for row in reader:
        vetor.append(row)# Adicionando cada linha do arquivo CSV a vetor



def ler_coluna_aventuras(caminho_arquivo_csv):
    aventuras = []
    # Lendo a coluna 'Aventuras' do arquivo CSV especificado
    with open(caminho_arquivo_csv, 'r') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            aventuras.append(linha['Aventuras:'])
    return aventuras

# Utilizando a função para ler a coluna "Aventuras"
aventuras = ler_coluna_aventuras('projeto.csv')
print("Conteúdo da coluna 'Aventuras':")
for aventura in aventuras:
    print(aventura)


def imprimir_aventura_especifica(caminho_arquivo_csv, indice):
    av_escolhida = []
    # Abrindo e lendo o arquivo CSV para imprimir uma aventura específica
    with open(caminho_arquivo_csv, 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            aventuras.append(linha['Aventuras:'])

    if 0 <= indice < len(aventuras):
        print(f"Aventura na posição {indice}: {aventuras[indice]}")
        print(f"opção na posição : {aventuras[opA]}")
        print(f"opção na posição : {aventuras[opB]}")

    else:
        print("Índice fora do intervalo.")

# Exemplo de uso da função para imprimir uma aventura específica escolhida pelo usuário
caminho_arquivo_csv = 'projeto.csv'
indice = int(input(f"Digite o índice da aventura que deseja imprimir (0 a 39): "))
imprimir_aventura_especifica(caminho_arquivo_csv, indice)
         
def remover_aventura(caminho_arquivo_csv, indice):
    aventuras = []
    # Ler aventuras do arquivo CSV
    with open(caminho_arquivo_csv, 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            aventuras.append(linha['Aventuras:'])
    # Verificar se o índice fornecido é válido
    if 0 <= indice < len(aventuras):
        aventura_removida = aventuras.pop(indice)
        print(f"Aventura removida: {aventura_removida}")
    else:
        print("Índice fora do intervalo.")
        return
    # Escrever de volta ao arquivo CSV sem a aventura removida
    with open(caminho_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        for aventura in aventuras:
            escritor.writerow([aventura])
    print("Lista atualizada de aventuras:")
    for aventura in aventuras:
        print(aventura)


        
# Exemplo de uso da função para remover uma aventura específica escolhida pelo usuário
caminho_arquivo_csv = 'projeto.csv'
indice = int(input(f"Digite o índice da aventura que deseja remover (0 a 39): "))
remover_aventura(caminho_arquivo_csv, indice)
