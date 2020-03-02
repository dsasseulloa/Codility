
import random

#a = int(input("digite o tamanho da Matriz: "))
#k = int(input("digite o numero de rotaçoes: "))
a=12
k=1
#a tamanho
#k rotacoes

def solucao(a,k):
    list = []
    lista = []
    while len(list) < a:
        for i in range(a):
            r = random.randint(0, a)
            if r not in list:
                list.append(r)
    print(list)

    for i in range(0,k):
        primeiro_num=list[0]

        for j in range(0,len(list)):
            if j != len(list)-1:
                print(list[j+1])

    list.insert(0,primeiro_num)
            # if j == len(list)-1:
            #     print("AAA")
            #     list[j] = list[j+1]

        # list[0] = primeiro_num
        # for j in range(0, len(list) - 1):
        #     list[j] = list[j + 1]
        #
        # list[len(list) - 1] = primeiro_num

    print(f"Rotaçao lista {k} vezes:")
    for i in range(0, len(list)):
        lista.append(list[i])

    print(lista)





solucao(a,k)
