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
                    print(n, path)
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n,path))
                    path.pop()
        return maxSheep
    
    answer = dfs(0,0,0,[0])
    return answer