import sys

sys.stdin = open("_암호문1.txt")

result = {}
for n in range(1, 11):
     
    while(1):
        N = int(input())
        if N>= 10 and N<=20:
            break

    A = list(map(str,input().split(' ')))
   
    while(1):
        num = int(input())
        if num>= 5 and num<=10:
            break

    B = list(map(str,input().split(' ')))
    
    for i in range(0, num):
        B.remove(B[0])
        index_ = int(B.pop(0))
        cnt = int(B.pop(0))
        for i in range(0, cnt):
            A.insert(index_,B.pop(0))
            index_ +=1
    result[n] = A[0:10]

for n in result:
    print(f'#{n}',end=' ')
    for i in result[n]:
        print(f"{i}",end=' ')
    print()
    