from random import randint

with open('text55.txt', mode='w+', encoding='utf-8') as my_f:
    my_f.write(" ".join([str(randint(1,1000)) for _ in range(100000)]))
    my_f.seek(0)
    print(sum(map(int, my_f.readline().split())))

