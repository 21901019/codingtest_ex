def solution(record):
    answer = []
    record_re = []
    dic_id = {}
    for i in record:
        record_re.append(i.split())
        
    for i in range(len(record)):
        if record_re[i][0] == "Enter":
            dic_id[record_re[i][1]] = record_re[i][2]
        elif record_re[i][0] == "Change":
            dic_id[record_re[i][1]] = record_re[i][2]
            
    for i in range(len(record)):
        if record_re[i][0] == "Enter":
            answer.append(dic_id[record_re[i][1]]+'님이 들어왔습니다.')
        elif record_re[i][0] == "Leave":
            answer.append(dic_id[record_re[i][1]] + '님이 나갔습니다.')
    return answer