'''전화번호가 다른 번호의 접두사인 경우 False'''
def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True 
    