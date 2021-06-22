def solution(expression):
    answer = 0
    expression = expression.replace('*', ' * ')
    expression = expression.replace('+', ' + ')
    expression = expression.replace('-', ' - ')
    list_expression = list(expression.split())
    reward = [0 for _ in range(6)]
    numbers = []
    operators = []
    case1 = case2 = case3 = case4 = case5= case6 = list_expression
    #case1 (+, -, *), case2 (+, *, -) case3 (-, +, *), case4 (-, *, +), case5 (*, +, -), case6 (*, -, +)
    for i in range(len(case1)):
        if case1[i] == '+':
            case1.insert(i, case1[i-1] + case1[i+1])
            del case1[i-1]
            del case1[i-1]
            del case1[i+1]
            #del case1[i-1], case1[i+1]
    print(case1)
    return answer