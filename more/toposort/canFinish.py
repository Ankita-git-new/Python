class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahns algorithm, topological sort
        adj = collections.defaultdict(list)
        degree = collections.Counter()
        
        for dest, orig in prerequisites:
            adj[orig].append(dest)
            degree[dest] += 1
        
        bfs = [c for c in range(numCourses) if degree[c] == 0]
        
        for o in bfs:
            for d in adj[o]:
                degree[d] -= 1
                if degree[d] == 0:
                    bfs.append(d)

        return len(bfs) == numCourses
        



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        degree = collections.Counter()
        
        for dest, orig in prerequisites:
            adj[orig].append(dest)
            degree[dest] += 1
            if orig not in degree:
                degree[orig] = 0
        
        free = set(range(numCourses))-set(degree)
        for f in free:
            degree[f] = 0
        
        stk = list(filter(lambda x: degree[x]==0, degree.keys()))
        
        cnt = 0
        while stk:
            node = stk.pop()
            cnt += 1
            for nei in adj[node]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    stk.append(nei)
        
        return cnt == numCourses