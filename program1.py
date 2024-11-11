class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Helper function to perform DFS
        def dfs(i, j):
            # Stack-based DFS to mark all land parts of an island as visited
            stack = [(i, j)]
            grid[i][j] = 'W'  # Mark as visited by converting to 'W'
            while stack:
                x, y = stack.pop()
                # Explore neighbors (up, down, left, right)
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 'L':
                        grid[nx][ny] = 'W'  # Mark as visited
                        stack.append((nx, ny))

        # Main logic to find islands
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':  # Found an unvisited land
                    dfs(i, j)  # Run DFS to mark the entire island
                    count += 1  # Increment island count
        return count
