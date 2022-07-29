import sys

sys.stdin = open("_직사각형길이찾기.txt")

case = int(input())
result = []
for i in range(1, case+1):
    a,b,c = map(int, input().split(' '))
    if a == b:
        result.append(c)
    elif a == c:
        result.append(b)
    else:
        result.append(a)

for i in range(0, case):
    print(f'#{i+1} {result[i]}')
    
    