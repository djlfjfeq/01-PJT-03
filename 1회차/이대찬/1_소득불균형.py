import sys

sys.stdin = open("_소득불균형.txt")

case = int(input())
result = []
for i in range(0, case):
    cnt = int(input())
    tmp = 0
    lst = list(map(int, input().split(' ')))
  
    for i in lst:
        if i <= sum(lst)/len(lst):
            tmp +=1
    result.append(tmp)
       
for i in range(0, case):
    print(f'#{i+1} {result[i]}')

 