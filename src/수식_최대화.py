from itertools import permutations
def solution(expression):
    answer = 0
    op_prioritys = list(permutations(['+', '-', '*']))
    for op_priority in op_prioritys:
        res = abs(int(recur_cal(op_priority, 0, expression)))
        answer = max(answer, res)
    return answer

def recur_cal(priority, depth, expresstion):
    if depth == 2:
        return str(eval(expresstion))
    if priority[depth] == '+':
        res = eval('+'.join([recur_cal(priority, depth+1, piece) for piece in expresstion.split('+')]))
    elif priority[depth] == '-':
        res = eval('-'.join([recur_cal(priority, depth+1, piece) for piece in expresstion.split('-')]))
    elif priority[depth] == '*':
        res = eval('*'.join([recur_cal(priority, depth+1, piece) for piece in expresstion.split('*')]))
    return str(res)