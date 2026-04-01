class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        INF = 2147483647


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
            
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    nr = r + dr 
                    nc = c + dc

                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == INF and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                

            dist += 1