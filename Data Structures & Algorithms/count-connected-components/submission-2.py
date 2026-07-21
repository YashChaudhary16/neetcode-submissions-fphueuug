class Solution:

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return
        
        if self.rank[pb] > self.rank[pa]:
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1
        self.count -= 1


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        self.count = n

        self.parent = [x for x in range(n)]
        self.rank = [0] * n

        for x, y in edges:
            self.union(x, y)
        
        return self.count