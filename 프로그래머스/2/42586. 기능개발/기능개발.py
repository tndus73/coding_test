def solution(progresses, speeds):
        arr = []
        answer = []

        for pro, spe in zip(progresses,speeds):
            if (100-pro)%spe == 0:
                arr.append((100-pro)//spe)
            else:
                arr.append((100-pro)//spe+1)
        
        standard = arr[0]
        count = 1
        
        for i in range(1,len(arr)):
            if arr[i] <= standard:
                count+=1
            else:
                answer.append(count)
                standard = arr[i]
                count = 1
        answer.append(count)    
        return answer