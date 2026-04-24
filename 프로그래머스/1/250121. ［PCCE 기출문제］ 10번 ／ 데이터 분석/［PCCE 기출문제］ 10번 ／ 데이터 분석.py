'''
def solution(data, ext, val_ext, sort_by):
    answer = []
    for row in data:
        if ext == "code":
            if row[0] < val_ext:
                answer.append(row)
        elif ext == "date":
            if row[1] < val_ext:
                answer.append(row)
        elif ext == "maximum":
            if row[2] < val_ext:
                answer.append(row)
        elif ext == "remain":
            if row[3] < val_ext:
                answer.append(row)
    if sort_by == "code":
        return sorted(answer, key=lambda x: x[0])
    elif sort_by == "date":
        return sorted(answer, key=lambda x: x[1])
    elif sort_by == "maximum":
        return sorted(answer, key=lambda x: x[2])
    else:
        return sorted(answer, key=lambda x: x[3])
'''

def solution(data, ext, val_ext, sort_by):
    idx = {'code' : 0, 'date' : 1, 'maximum' : 2, 'remain' : 3}
    answer = []
    
    for row in data:
        if row[idx[ext]] < val_ext:
            answer.append(row)
            
    return sorted(answer, key=lambda x: x[idx[sort_by]])        