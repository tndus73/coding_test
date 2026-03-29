def solution(s):
    num_dict = {
        "0" :	"zero",
        "1" :	"one",
        "2" :	"two",
        "3" :	"three",
        "4" :	"four",
        "5" :	"five",
        "6" :	"six",
        "7" :	"seven",
        "8" :	"eight",
        "9" :	"nine"
    }
    
    for key, value in num_dict.items():
        s = s.replace(value,key)
        #문자열에서 value값찾아서 key로 바꿔라
    return int(s)
