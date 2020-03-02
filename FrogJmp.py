
#x posiçao do sapo 10 ou 1
#y posiçao que o sapo vai 85 ou 5.
#D distancia que ele pulou 30 ou 2

def solution(X, Y, D):
    return int((Y-X + D - 1)/D)


    # if X+(int(Y/D))<=Y:
    #
    #     print(X+(int(Y/D)))

    # if D*(Y/D)+X >= Y:
    #     a=((Y+X)/D)
    #     return int(a)

# count = 0
# while X < Y:
#     X += D
#     count += 1
# return count


print(solution(10,85,30))
print(solution(1,5,2))

















num=2.9
print(int(num))