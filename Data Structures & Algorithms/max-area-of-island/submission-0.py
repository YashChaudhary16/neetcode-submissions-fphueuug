class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        max_area = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def traverse(r, c):
            area = 1
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1
                
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = traverse(r, c)
                    max_area = max(max_area, area)


        return max_area
