def solution(video_len, pos, op_start, op_end, commands):
    video_len = int(video_len[:2]) * 60 + int(video_len[3:])
    pos = int(pos[:2]) * 60 + int(pos[3:])
    op_start = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end = int(op_end[:2]) * 60 + int(op_end[3:])

    if op_start <= pos <= op_end:
        pos = op_end
    for com in commands:
        if com == 'prev':
            pos = max(0, pos-10)
        else:
            pos  = min(video_len, pos+10)
            
        if op_start <= pos <= op_end:
            pos = op_end
        
    return str(pos//60).zfill(2) + ':' + str(pos%60).zfill(2) 