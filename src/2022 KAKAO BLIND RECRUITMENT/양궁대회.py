# 백트래킹
def solution(n, info):
    def cal_score(a_list, l_list): #return 최종 점수 차이
        #라이언이 이기면 +, 어피치가 이기면 -
        l_score, a_score = 0, 0
        for i in range(11):
            if a_list[i] == l_list[i] == 0:
                continue
            elif a_list[i] >= l_list[i]:
                a_score += 10 - i
            elif a_list[i] < l_list[i]:
                l_score += 10 - i
        return l_score - a_score
    
    def recursion(n, layer)
    answer = []
    return answer