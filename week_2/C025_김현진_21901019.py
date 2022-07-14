def solution(left, right):
    answer = 0
    sub = 0
    tot = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i%j == 0:
                sub += 1
        if sub % 2 == 1:
            tot -= i
        else:
            tot += i
        sub = 0
    answer = tot
    return answer