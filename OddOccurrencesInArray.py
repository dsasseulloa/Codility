

# def Solution(A):
#     print(A.count(2))
#
#     # for i in A:
#     #     if A.count(i) < 2:
#     #         return i



def solution(A):
    if len(A) == 1:
         return A[0]
    A = sorted(A)
    print("sorted A: ",A)
    print("len A: ",len(A) )
    print("")
    for i in range(0 , len (A) , 2):
         print("i: ",i)
         print("i+1: ",i+1)
         print("")
         if i+1 == len(A):
             print("if1")
             return A[i]

         if A[i] != A[i+1]:
             print(i)
             print(A[i])
             print("if2")
             return A[i]

print(solution([2,2,5,5]))

