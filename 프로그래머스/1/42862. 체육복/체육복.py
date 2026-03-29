def solution(n, lost, reserve):

    lost_set = set(lost)
    reserve_set = set(reserve)
    both = lost_set & reserve_set
    lost_set -= both
    reserve_set -= both
    
    for i in sorted(lost_set):
        if i-1 in reserve_set:
            reserve_set.remove(i-1)
        elif i+1 in reserve_set:
            reserve_set.remove(i+1)
        else:
            n -= 1
    return n