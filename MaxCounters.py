

N=5
A=[3,4,4,6,1,4,4]


def solution(N, A):
    n_counter=[0]*N
    contador_max = 0
    contador_atual=0
    print(n_counter)
    for i in A:

        if 1 <= i <= N:
            if contador_max > n_counter[i-1]:
                n_counter[i-1] = contador_max
            n_counter[i-1] +=1
            if contador_atual < n_counter[i-1]:
                contador_atual = n_counter[i-1]
        else:
            contador_max=contador_atual
    for i in range(0,N):
        if n_counter[i]<contador_max:
            n_counter[i]=contador_max
    return n_counter


print(solution(N,A))