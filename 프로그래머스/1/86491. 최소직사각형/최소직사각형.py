
def solution(sizes):
    sw = []
    sh = []
    for w, h in sizes:
        sw.append(max(w,h))
        sh.append(min(w,h))
    return int(max(sw)) * int(max(sh))    