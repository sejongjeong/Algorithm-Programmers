def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))] # answer list의 순서는 id_list의 순서와 동일
    record = {}
    order = {} # order dict는 id_list의 index를 저장
    for i, id in enumerate(id_list):
        record[id] = set() #record dict의 Value는 중복을 체크해야하기 때문에 Set을 사용하는 것이 효율적
        order[id] = i
    for r in report:
        reporter, reported = r.split()
        record[reported].add((reporter))
    for value in record.values():
        if len(value) >= k:
            for reporter in value:
                answer[order[reporter]] += 1
    return answer