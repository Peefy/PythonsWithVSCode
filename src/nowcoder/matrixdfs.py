
def _dfs(rows, columns, grid, i, j, isvisited):
    if i < 0 or i > rows:
        return False
    if j < 0 or j > columns:
        return False
    if grid[i][j] == 0 or isvisited[i][j] == 1:
        return False
    if grid[i][j] == 9:
        return True
    isvisited[i][j] == 1
    return _dfs(rows, columns, grid, i + 1, j, isvisited) or \
        _dfs(rows, columns, grid, i, j + 1, isvisited) or \
        _dfs(rows, columns, grid, i - 1, j, isvisited) or \
        _dfs(rows, columns, grid, i, j - 1, isvisited)


def isPath(rows, columns, grid):
    isvisited = [[0] * columns for i in range(rows)]
    return _dfs(rows, columns, grid, 0, 0, isvisited)
    
print(isPath(3, 3, [[1, 1, 1], [1, 9, 1], [0, 0, 0]]))
print(isPath(3, 3, [[1, 0, 1], [0, 9, 1], [0, 0, 0]]))
print(isPath(3, 3, [[1, 1, 1], [0, 0, 1], [0, 0, 9]]))
