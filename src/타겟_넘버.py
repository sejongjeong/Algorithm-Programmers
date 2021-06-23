cnt = 0
def solution(numbers, target):
    answer = 0
    numbers_len = len(numbers)
    recur_cal(0, 0, numbers, target, numbers_len)
    answer = cnt
    return answer

def recur_cal(res, depth, numbers, target, numbers_len):
    global cnt
    if depth == numbers_len:
        if res == target:
            cnt += 1
        return
    for i in range(2):
        if i:
            recur_cal(res-numbers[depth], depth+1, numbers, target, numbers_len)
        else:
            recur_cal(res+numbers[depth], depth+1, numbers, target, numbers_len)