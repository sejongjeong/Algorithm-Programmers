from collections import defaultdict

def solution(info, edges):
    eg = defaultdict(list)
    for p, c in edges:
        eg[p].append(c)
    
    def dfs(sheep, wolf, current, path):
        if info[current]:
            wolf+=1
        else:
            sheep += 1
        if sheep <= wolf:
            return 0
        
        maxSheep = sheep
        
        for p in path:
            for n in eg[p]:
                if n not in path:
                    path.append(n)
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n,path))
                    path.pop()
        return maxSheep
    
    answer = dfs(0,0,0,[0])
    return answer

# from collections import defaultdict

# answer = 0
# def solution(info, edges):
#     eg = defaultdict(list)
#     for s, d in edges:
#         eg[s].append(d)
#     def backtraking(sheep, wolf, node, path):
#         global answer
#         sheep += info[node] ^ 1
#         wolf += info[node]
#         if sheep <= wolf:
#             return
#         answer = max(answer, sheep)
#         for p in path:
#             for n in eg[p]:
#                 if n not in path:
#                     path.append(n)
#                     backtraking(sheep, wolf, n, path)
#                     path.pop()
#     backtraking(0,0,0,[0])
#     return answer