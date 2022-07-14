import copy
def solution(skill, skill_trees):
    answer = 0
    idx = []
    idx_co = []
    for j in skill_trees:
        for id, i in enumerate(skill):
            if i in j:
                if id > 0:
                    if j.find(skill[id-1]) in idx:
                        idx.append(j.find(i))
                    else:
                        idx = [1, 0]
                if id == 0:
                    idx.append(j.find(i))
        idx_co = copy.deepcopy(idx)
        idx.sort()
        
        if idx_co == idx or len(idx) == 0:
            answer += 1
        idx_co = []
        idx = []
        
    if answer == 0:
        answer = -1
    return answer