
A=[1, 2, 3, 4, 5]

def solution(A):
    A.sort()

    A=list(set(A))
    if max(A) <= 0:
        return 1

    num_maior = 1
    while num_maior in A:
        num_maior += 1
    return num_maior



print("resultado: ",solution(A))
