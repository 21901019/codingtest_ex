#a = int(input())
#b = int(input())

a = 3
b = 10

st = b - 1 #lst[0]+lst[1]-lst[0]-1
end = b-a

kid = 1
mom = 1

#for idx, i in enumerate(range(st, 0, -1)):
#    kid *= i
#    if idx == end-1:
#        break
for i in range(end):
    kid *= (st-i)
for i in range(1, end+1):
    mom *= i

print(int(kid/mom))
