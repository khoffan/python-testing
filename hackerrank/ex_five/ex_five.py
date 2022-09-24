def gridChallenge(grid):
    # Sort each row.
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
        
    # Check each column is sorted.
    for i in range(len(grid[0])):
        column_list = []
        for j in range(len(grid)): 
            column_list.append(grid[j][i])
        if (column_list != sorted(column_list)):
            return "NO"
            
    return "YES"