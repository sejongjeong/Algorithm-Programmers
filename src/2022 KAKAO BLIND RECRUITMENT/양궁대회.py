# 백트래킹
def solution(n, info):
    def cal_score(a_list, l_list):  # return 최종 점수 차이
        # 라이언이 이기면 +, 어피치가 이기면 -
        l_score, a_score = 0, 0
        for i in range(11):
            if a_list[i] == l_list[i] == 0:
                continue
            elif a_list[i] >= l_list[i]:
                a_score += 10 - i
            elif a_list[i] < l_list[i]:
                l_score += 10 - i
        return l_score - a_score

    def return_lots_of_low_score_list(list1, list2): # 점수가 같을시 낮은 점수가 많은 list를 return
        for i in range(10, -1, -1):
            if list1[i] > list2[i]:
                return list1
            elif list1[i] < list2[i]:
                return list2

    max_score = 0
    tmp_list = []
    answer = []

    def recursion(left, layer):
        nonlocal max_score, tmp_list, answer
        if layer == 11 and left == 0:
            tmp = cal_score(info, tmp_list)
            if max_score < tmp:
                max_score = tmp
                answer = tmp_list[:]
            elif max_score != 0 and max_score == tmp:
                answer = return_lots_of_low_score_list(answer, tmp_list)[:]
            return
        elif layer == 11:
            return
        for i in range(left + 1):
            tmp_list.append(i)
            recursion(left - i, layer + 1)
            tmp_list.pop()

    recursion(n, 0)
    if max_score == 0:
        answer = [-1]
    return answer


#0점으로 가까운 점수가 가장 많게
# 백트래킹
def solution(n, info):
    def cal_score(a_list, l_list): #return 최종 점수 차이
        #라이언이 이기면 +, 어피치가 이기면 -
        l_score, a_score = 0, 0
        for i in range(11):
            if a_list[i] == l_list[i] == 0:
                continue
            elif a_list[i] >= l_list[i]:
                a_score += i
            elif a_list[i] < l_list[i]:
                l_score += i
        return l_score - a_score
    
    max_score = 0
    tmp_list = []
    answer = []
    
    def recursion(left, layer):
        nonlocal max_score, tmp_list, answer
        if layer == 11 and left == 0:
            tmp = cal_score(info[::-1], tmp_list)
            if max_score < tmp :
                max_score = tmp
                answer = tmp_list[::-1]
            return
        elif layer == 11:
            return
        for i in range(left, -1, -1):
            tmp_list.append(i)
            recursion(left - i, layer + 1)
            tmp_list.pop()
    recursion(n, 0)
    if max_score == 0:
        answer = [-1]
    return answer