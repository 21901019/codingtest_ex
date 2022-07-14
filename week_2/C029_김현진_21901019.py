#lst = list(map(int, input().split()))

lst = [2100000000, 9, 10]
x = 1
if lst[1] >= lst[2]:
    print(-1)
else:
    print(int(lst[0]/(lst[2]-lst[1])+1))
