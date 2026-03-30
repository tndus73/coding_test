def solution(files):
    answer = []
    for file in files:
        head =''
        number =''
        i = 0
        
        while i < len(file) and not file[i].isdigit():
            head += file[i]
            i += 1
        
        while i < len(file) and file[i].isdigit():
            number += file[i]
            i += 1
        answer.append((head, int(number), file))
    answer.sort(key=lambda x: (x[0].lower(),x[1]))    
    return [x[2] for x in answer]