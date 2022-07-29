import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

result = []

for i in range(0, T):
    num = int(input())
    lst = list(map(int,(input().split())))
    tmp = {}
    tmp_lst = []
    for i in lst:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] = tmp[i] + 1
    max_ = max(list(tmp.values()))
    
    for i in tmp:
        if tmp[i] == max_:
            tmp_lst.append(i)
    result.append(max(tmp_lst))
    
for i in range(0,len(result)):
    print(f'#{i+1} {result[i]}')
            
        
    