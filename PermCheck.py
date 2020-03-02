
A=[4, 1, 3, 2]

def solution(A):
    num_total=max(A)
    print("num total",num_total)
    A.sort
    setlist=list(set(A))
    print(A)
    print("len A", len(A))
    if len(A) > num_total or len(A) < num_total:
        print("len A",len(A))
        return 0
    print("")
    print(setlist)
    if len(setlist)+1 != num_total:
        prox_num=1
        for prox_num in range(1,len(setlist)):
            print(prox_num)
            prox_num+=1
            if prox_num not in setlist:
                return 0
        return 1
    return 0



print("return ",solution(A))