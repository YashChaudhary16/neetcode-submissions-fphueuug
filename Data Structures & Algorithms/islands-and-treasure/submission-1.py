class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        land = 2147483647

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        time = 0
        while queue:
            time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == land:
                        grid[nr][nc] = time
                        queue.append((nr, nc))
        
        