def solution(genres, plays):
    dic_sum = {}
    dic = {}
    answer = []
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        # 1. 장르별 총 재생 수
        dic_sum[genre] = dic_sum.get(genre,0) + play
        # 2. 장르별 노래 목록
        if genre not in dic:
            dic[genre] = []
        dic[genre].append((idx, play))
    # 총 재생 수 높은 장르 순서대로 정렬    
    dic_sum = sorted(dic_sum.items(), key = lambda x:x[1], reverse=True)

    for genre, sum_play in dic_sum:
        # 해당 장르 안에서 재생 수 내림차순, 같으면 고유번호 오름차순
        dic[genre].sort(key=lambda x:(-x[1],x[0]))
        # 최대 2개 뽑기
        for idx, play in dic[genre][:2]:
            answer.append(idx)
    return answer