n = int(input())
numlist = list(map(int, input().split()))
#둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. for문 쓰면 "한 줄에 정수를 하나씩" 입력됨
    
print(min(numlist), max(numlist))