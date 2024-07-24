import csv
import random

# Inicializando a lista para armazenar as aventuras
av = []

# Lendo o conteúdo do arquivo 'objetivo.txt'
with open('Objetivo.txt', 'r') as arquivo:
    obj = arquivo.read()

# Lendo o conteúdo do arquivo 'projeto.csv'
with open('projeto.csv', 'r') as arquivo:
    aventura = csv.DictReader(arquivo)
    for i in aventura:
        av.append(i)

# Função para imprimir todas as aventuras
def imprime_aventura(copia_v):
    for k in copia_v:
        print(f"av: {k['Aventuras']}")


# Função para imprimir uma aventura específica
def imprime_escolhida(copia_v, n):
    for k in copia_v:
        if k==copia_v[n]:
            print()
            print(f"av{n}: {k['Aventuras']}")
            print()
            print(f"opção A: {k['opA']}")
            print(f"opção B: {k['opB']}")
            escolha = input("Escolha uma opção (A ou B): ").strip().upper()
            if escolha == 'A':
                probabilidade_a = k['probSA']
            elif escolha == 'B':
                probabilidade_b = k['probSB']
            else:
                print("Opção inválida. Tente novamente.")
                return
            n_a = random.randint(0,100)
            if n_a < probabilidade_a:
                print("msgSA")
            if n_a > probabilidade_a:
                print("msgFA")
            if n_a < probabilidade_b:
                print("msgSA")
            if n_a > probabilidade_b:
                print("msgFA")


# Função para excluir uma aventura específica
def exclui_especifica(copia_v, n):
    copia_v.pop(n)
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
av1 = random.randint(0, 39)
print(len(av))  
imprime_escolhida(av, av1)
av = exclui_especifica(av, av1)
print(len(av))
