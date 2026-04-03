class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [x for x in range(len(edges))]
        rank = [1] * len(edges)

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(node1, node2):
            node1, node2 = find(node1), find(node2)

            if node1 == node2:
                return True
            
            if rank[node1] > rank[node2]:
                parent[node2] = node1
                rank[node1] += rank[node2]
            
            else:
                parent[node1] = node2
                rank[node2] += rank[node1]
            
            return False
        
        redundant_connections = []
        for [node1, node2] in edges:
            if union(node1 - 1, node2 - 1):
                redundant_connections.append([node1, node2])
        return redundant_connections[-1]


