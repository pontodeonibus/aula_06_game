import random

n = [2,1,0]
j1 = input('Jogador 1: ')
j2 = input('Jogador 2: ')
for c in n:
    n = random.randint(1,2)
    j1_numero = int(input('Jogador Nº1, Escolha um número: '))
    j2_numero = int(input('Jogador nº2, Escolha um número: '))
    if j1_numero == n and j2_numero == n:
        print('Empate') 
        break   
    if n == j1_numero:
        c = c -1 
        print(f"{j1} ganhou")
        break
    elif n == j2_numero:
        print(f"{j2} ganhou")
        break
    elif n != j1_numero and j2_numero and c <= 0:
        print(f'Vocês erraram, o número era {n}, suas chances esgotaram')
    else:
        print(f'Vocês erraram, o número era {n}, restam apenas {c} chances')

       
