av = []

with open('objetivo.txt', 'r') as arquivo:
    obj = arquivo.read()

with open('projeto.csv', 'r') as arquivo:
    aventura = csv.DictReader(arquivo)
    for i in aventura:
        av.append(i)

def imprime_avntura(copia_v):
    for h in copia_v:
        print(f"av:{k[Aventuras:]}")

def imprime_escolhida