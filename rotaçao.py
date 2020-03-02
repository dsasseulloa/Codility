def solution(a, k):
    if a == []:
        return a
    for time in range(k):
        last = a.pop(-1)
        a.insert(0, last)
    return a

print(solution([],1))