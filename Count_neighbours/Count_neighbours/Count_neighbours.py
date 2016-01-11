def count_neighbours(grid, row, col):
    row_inf = row - 1 if row > 0 else None
    col_inf = col - 1 if col > 0 else None
    row_sup = row + 1 if row + 1 < len(grid) else None 
    col_sup = col + 1 if col + 1 < len(grid[row]) else None
    col_sup_plus1 = col_sup + 1 if col_sup is not None else None

    return (sum(grid[row_inf][col_inf:col_sup_plus1]) if row_inf is not None else 0) + \
        (grid[row][col_inf] if col_inf is not None else 0) + \
        (grid[row][col_sup] if col_sup is not None else 0) + \
        (sum(grid[row_sup][col_inf:col_sup_plus1]) if row_sup is not None else 0)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
