def solution(s):
    answer = 0
    num = 1
    cnt = 0
    res = []
    for i in range(1, int(len(s)/2)+2):
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+i+i]:
                num += 1
            else:
                if num > 1:
                    cnt = cnt - num*i + i+int(num/10)+1
                    # if num > 9:
                    #     cnt = cnt - num*i + i+2
                    # else:
                    #     cnt = cnt - num*i + i+1
                num = 1
            if j+i > len(s):
                cnt += len(s)-j
                break
            cnt += i
        res.append(cnt)
        cnt = 0

    answer = min(res)
    return answer