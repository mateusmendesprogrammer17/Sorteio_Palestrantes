import random
palestrante_mateus=1 

palestrante_jean =2



for i in range(10):
    sorteio=random.randint(1,2);
    if sorteio==1:
        
        print (f"\nMateus {sorteio}")
    else:
        print(f"\nJean {sorteio}")


