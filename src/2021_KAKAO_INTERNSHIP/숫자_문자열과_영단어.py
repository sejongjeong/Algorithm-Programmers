def solution(s):
    answer = ''
    check = False
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tmp = ''
    for i,c in enumerate(list(s)):
        if c.isdigit():
            answer += c
            continue
        tmp += c
        if tmp in num_list:
            answer += str(num_list.index(tmp))
            tmp = ''
    return int(answer)