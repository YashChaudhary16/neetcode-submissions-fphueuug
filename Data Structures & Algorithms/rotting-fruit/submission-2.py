class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten_oranges = deque()
        fresh_count = 0

        # 1. Initial scan: Find rotten oranges AND count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_oranges.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # If there are no fresh oranges, it takes 0 minutes
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while rotten_oranges and fresh_count > 0:
            minutes += 1
            # Process current layer
            for _ in range(len(rotten_oranges)):
                r, c = rotten_oranges.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == 1):
                        
                        grid[nr][nc] = 2 # Mark as rotten
                        fresh_count -= 1 # One less fresh orange
                        rotten_oranges.append((nr, nc))
        
        # If fresh_count is still > 0, some oranges were unreachable
        return minutes if fresh_count == 0 else -1