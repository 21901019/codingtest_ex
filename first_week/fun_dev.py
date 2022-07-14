def solution(progresses, speeds):
    answer = []
    cnt = 0

    while len(progresses) != 0:
        for i in range(0, len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] > 100:
                progresses[i] = 100
        if progresses[0] == 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            if len(progresses) == 0:
                answer.append(cnt)
                break

            while progresses[0] == 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
                if len(progresses) == 0:
                    break

            answer.append(cnt)
            cnt = 0
    return answer