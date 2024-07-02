import csv

# Inicializando a lista para armazenar as aventuras
av = []

# Lendo o conteúdo do arquivo 'objetivo.txt'
with open('objetivo.txt', 'r') as arquivo:
    obj = arquivo.read()

# Lendo o conteúdo do arquivo 'projeto.csv'
with open('projeto.csv', 'r') as arquivo:
    aventura = csv.DictReader(arquivo)
    for i in aventura:
        av.append(i)

# Função para imprimir todas as aventuras
def imprime_aventura(copia_v):
    for k in copia_v:
        print(f"av: {k['Aventuras:']}")


# Função para imprimir uma aventura específica
def imprime_escolhida(copia_v, n):
    for k in copia_v:
        if k == n:
            print(f"av: {k['Aventuras:']}")

# Função para excluir uma aventura específica
def exclui_especifica(copia_v, n):
    for k in copia_v:
        if k == n:
            copia_v.pop(k)
    return copia_v

def continua(palavra):
    entrada = ""
    while entrada != palavra:
        entrada = input("Digite 's' para dar continuidade: ")
        if entrada != palavra:
            print("Palavra incorreta. Tente novamente.")
    print("Palavra confirmada, autorização concedida")



print(obj)
continua("s")
print("O programa foi retomado.")
imprime_aventura(av)
av1 = input("escolha uma aventura de 0 a 39 ")
imprime_escolhida(av, av1)
av = exclui_especifica(av, av1)
print("FIM...")












