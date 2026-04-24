def solution(mats, park):
    mats.sort(reverse=True)
    h = len(park)
    w = len(park[0])
    
    for size in mats:
        for i in range(h-size+1):
            for j in range(w-size+1):
                possible = True
                
                for x in range(i, i+size):
                    for y in range(j, j+size):
                        if park[x][y] != '-1':
                            possible = False
                            break
                    if not possible:
                        break
                if possible:
                    return size
    return -1