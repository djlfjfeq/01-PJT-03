import sys

sys.stdin = open("_문자열의거울상.txt")

case = int(input())
result = []
for i in range(0, case):
    str_ = input()
    result_str = ''
    tmp = ''
    for i in str_:
        if i == 'b':
            tmp = 'd'
            
        elif i == 'q':
            tmp = 'p'

        elif i == 'd':
            tmp = 'b'
            
        elif i == 'p':
            tmp = 'q'
            
        result_str = tmp + result_str 
    result.append(result_str)
       
for i in range(0, case):
    print(f'#{i+1} {result[i]}')

 