import sys

sys.stdin = open("_신용카드만들기1.txt")

case = int(input())
result = []
for i in range(0, case):
    t1 = 0
    t2 = 0
    lst = list(map(int, input().split(' ')))
    for i in range(0,len(lst)):
        if i % 2 == 0:
            t1 += lst[i]*2
        else:
            t2 += lst[i]
    if (t1+t2)%10 == 0:
        result.append(0)
    else:
        result.append(10-((t1+t2)%10))
       
for i in range(0, case):
    print(f'#{i+1} {result[i]}')

 