# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

# Example 1:
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]

# Example 2:
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105


def equalPairs(grid):
    # keep count of the Equal Row and Column Pairs count
    equal_row_and_columns_pairs_count = 0
    # two hashmaps to track the number of times each row and column appears
    row_pairs = {}
    column_pairs = {}
    for row in range(len(grid)):
        # make lists for each row and column
        row_list = grid[row]
        column_list = []
        # construct the column list
        for column in range(len(grid)):
            column_list.append(grid[column][row])
        # using tuples for hashing, each tuple represents a row or a column, respectively
        tuple_row = tuple(row_list)
        tuple_column = tuple(column_list)
        # set or increment the count for each row tuple and column tuple seen, respectively.
        row_pairs[tuple_row] = row_pairs.get(tuple_row, 0) + 1
        column_pairs[tuple_column] = column_pairs.get(tuple_column, 0) + 1
    # iterate through any of the pairs, in this case: the row pairs
    for current_pair in row_pairs:
        # the current pair has been seen in the columns
        if current_pair in column_pairs:
            # the amount of pairs possible of any array is the direct product of both frequencies,
            # then add that pair count to the final count
            equal_row_and_columns_pairs_count += (
                row_pairs[current_pair] * column_pairs[current_pair]
            )
    # return the count of equal row and column pairs
    return equal_row_and_columns_pairs_count

test_cases = [
    ([[3,2,1],
      [1,7,6],
      [2,7,7]], 1),

    ([[3,1,2,2],
      [1,4,4,5],
      [2,4,2,2],
      [2,4,2,2]], 3),

    ([[1,2],
      [2,1]], 2),

    ([[1,2],
      [3,4]], 0),

    ([[1,1],
      [1,1]], 4),

    ([[5]], 1),

    ([[1,2,1],
      [1,2,1],
      [3,4,3]], 0)
]

for i, (grid, expected) in enumerate(test_cases, 1):
    result = equalPairs(grid)
    print(f"Test {i}: {'PASS' if result == expected else 'FAIL'} — got {result}, expected {expected}")
