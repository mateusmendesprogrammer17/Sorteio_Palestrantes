import random

primeiroPalestrante = "Mateus"
segundoPalestrante = "Jean"
numeroDeSorteios = 10

for i in range(numeroDeSorteios):
    sorteio = random.randint(1, 2)
    if sorteio == 1:
        print(f"\n{primeiroPalestrante} foi sorteado: {sorteio}")
    else:
        print(f"\n{segundoPalestrante} foi sorteado: {sorteio}")
