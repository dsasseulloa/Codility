
# A = lista - "A[K] represents the position where one leaf falls at time K, measured in seconds."
# K = segundos
#
X=3
A= [1, 3, 1, 3, 1, 1, 2]

def solution(X,A):
    folhas_a_serem_percorridas=[-1]*X
    folhas_percorridas = 0
    for index,elemento in enumerate(A):
        print(index,elemento)
        print(folhas_a_serem_percorridas)
        if folhas_a_serem_percorridas[elemento-1] == -1:
            folhas_a_serem_percorridas[elemento - 1]=index
            folhas_percorridas+=1
            if folhas_percorridas==X:
                return index
    return -1

# def solution(X,A):
#
#     covered = 0
#     covered_a = [-1]*X
#     print(A)
#     print("covered_a: ",covered_a)
#     for index,element in enumerate(A):
#
#         print(index,element)
#         if covered_a[element-1] == -1:
#             print("passou")
#             covered_a[element-1] = element
#             covered += 1
#             print("covered_a: ", covered_a)
#             if covered == X:
#                 print(index)
#                 return index
#     return -1

    # A_sorted=sorted(A)
    # print(A)
    # if 1 not in A:
    #     print("if '1' not in A")
    #     print("not in a")
    #     return -1
    # for i in range(0,len(A_sorted)):
    #     if A_sorted[i] - A_sorted[i-1] > 1:
    #         print("n tem na lista")
    #         return -1
    # if X != max(A):
    #     print("fudeo")
    #     return -1
    # return A.index(max(A))


    # for i in range(len(A)):
    #     x=A.count(i)
    #     if A[i] == X:
    #         print("a",A[i])
    #         res = i
    #     if A[len(A)-1] != X and res == 0:
    #         res = -1
    #     if x==len(A):
    #         return -1
    # return res


a=solution(X,A)
print("resultado: ",a)

