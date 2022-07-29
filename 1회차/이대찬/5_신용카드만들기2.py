import sys

sys.stdin = open("_신용카드만들기2.txt")

number= '0123456789'
start = '34569'
case = int(input())
result = []
for i in range(0, case):
    card = input()
    cnt = 0
    if card[0] not in start:
        result.append(0)
        continue  #if문 break
    
    for n in card:
        if n in number:
            cnt += 1
        elif n != '-':
            result.append(0)
            break
    if cnt == 16:
        result.append(1)
    else:
        result.append(0)
       
for i in range(0, len(result)):
    print(f'#{i+1} {result[i]}')

