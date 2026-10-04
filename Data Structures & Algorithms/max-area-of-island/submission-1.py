class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()

        area=0

        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visit.add((r,c))
            count=1

            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    nr,nc=row+dr,col+dc

                    if nr>=rows or nc>=cols or nr<0 or nc<0 or grid[nr][nc]==0 or (nr,nc) in visit:
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))

                    count+=1
            return count            
                

            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    area=max(area,bfs(r,c))
        return area
        