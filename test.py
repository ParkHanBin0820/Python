#프로그래머스 같은숫자는 싫어

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0: #처음은 answer에 저장
            answer.append(arr[i]) #answer에 arr list 저장
        elif arr[i] != arr[i-1]: #arr의 전 값이 arr와 같이 않을 경우 
            answer.append(arr[i]) #저장
    return answer 