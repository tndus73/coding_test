#반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용(개행문자가 같이 입력)
#sys.stdin.readline().strip()쓰면 양쪽 끝에 있는 공백 문자 제거
#input()사용하면 시간초과

import sys

string = [sys.stdin.readline().strip() for _ in range(3)]

for i in range(3):
    if string[i].isdigit():    #문자열이 모두 숫자로 이뤄져있는지 확인
        answer = int(string[i])+(3-i)
        break

if answer % 15 == 0:
    print('FizzBuzz')
elif answer % 3 == 0:
    print('Fizz')
elif answer % 5 == 0:
    print('Buzz')
else:
    print(answer)