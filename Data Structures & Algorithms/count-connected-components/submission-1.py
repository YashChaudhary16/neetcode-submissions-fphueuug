class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = collections.defaultdict(list)
        visited = set()
        
        connected_components = 0

        for [a, b] in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        nodes = [x for x in range(n)]
        
        def dfs(node):
            q = collections.deque()
            q.append(node)

            while q:
                node = q.pop()
                visited.add(node)
                
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        q.append(neighbor)


        for node in nodes:
            if node not in visited:
                connected_components += 1
                dfs(node)
        

        return connected_components
        

        

        

