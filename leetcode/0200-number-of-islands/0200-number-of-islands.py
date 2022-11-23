class Solution(object):
    myGrid = []
    def dfs(self,i,j):
        if (i<0 or i>=len(self.myGrid)) or (j<0 or j>=len(self.myGrid[0])) or self.myGrid[i][j] != "1":
            return

        self.myGrid[i][j]="0"
        self.dfs(i+1,j)
        self.dfs(i-1,j)
        self.dfs(i,j+1)
        self.dfs(i,j-1)

    def numIslands(self, grid):
        self.myGrid = grid
        count=0
        if not grid :
            return 0 
        for i in range(len(self.myGrid)):
            for j in range(len(self.myGrid[0])):
                if(self.myGrid[i][j] =='1'):
                    self.dfs(i,j)
                    count+=1

        return count
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        