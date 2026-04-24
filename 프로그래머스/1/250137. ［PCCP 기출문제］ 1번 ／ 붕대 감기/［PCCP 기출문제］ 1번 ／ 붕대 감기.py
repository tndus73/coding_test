def solution(bandage, health, attacks):
    t, x, y = bandage
    hp = health  #현재채력
    time = 0    #현재시간
    combo = 0   #연속 성공 횟수

    for attack_time, damage in attacks: 
        while time < attack_time -1: #공격 전까지 회복
            time += 1
            combo += 1
            
            hp += x
            if combo == t:
                hp += y
                combo = 0
            
            if hp > health:
                hp = health
        
        #공격 받기
        time = attack_time
        hp -= damage
        combo = 0
        
        if hp <= 0 :
            return -1
    return hp
