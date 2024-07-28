import csv
import random

# Inicializando a lista para armazenar as aventuras
av = []

# Lendo o conteúdo do arquivo 'Objetivo.txt'
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
        if k == copia_v[n]:
            print()
            print(f"aventura {n}: {k['Aventuras']}")
            print()
            print(f"opção A): {k['opA']}")
            print(f"opção B): {k['opB']}")
            escolha = input("Escolha uma opção (A ou B): ").upper()
            n_a = random.randint(0, 100)
            if escolha == 'A':
                probabilidade_a = int(k['probSA'])
                if n_a < probabilidade_a:
                    print(k['msgSA'])
                else:
                    print(k['msgFA'])
            elif escolha == 'B':
                probabilidade_b = int(k['probSB'])
                if n_a < probabilidade_b:
                    print(k['msgSB'])
                else:
                    print(k['msgFB'])
            else:
                print("Opção inválida. Tente novamente.")
                return
            continua("s")


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

n = 39
print(obj)
continua("s")
print("O programa foi retomado.")
imprime_aventura(av)
av1 = random.randint(0, n)
print(len(av))  

while n > 0:
    imprime_escolhida(av, av1)
    av = exclui_especifica(av, av1)
    n = len(av)
    if n > 0:
        av1 = random.randint(0, n-1)
    else:
        print("Parabéns! Você completou todas as aventuras.")
        break
    print(len(av))