class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = []

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.add((r, c))
                if r == (rows - 1) or c == (cols - 1):
                    atlantic.add((r, c))
        
        pq = deque(pacific)
        pac = set()
        while pq:
            (r, c) = pq.popleft()
            pac.add((r, c))

            for dr, dc in directions:
                row = dr + r
                col = dc + c

                if (row in range(rows) and
                    col in range(cols) and
                    heights[row][col] >= heights[r][c] and
                    (row, col) not in pac):
                    pq.append((row, col))
        
        aq = deque(atlantic)
        atl = set()
        while aq:
            (r, c) = aq.popleft()
            atl.add((r, c))

            for dr, dc in directions:
                row = dr + r
                col = dc + c

                if (row in range(rows) and
                    col in range(cols) and
                    heights[row][col] >= heights[r][c] and
                    (row, col) not in atl):
                    aq.append((row, col))
            
        res = []
        for r, c in atl:
            if (r, c) in pac:
                res.append([r, c])
        return res