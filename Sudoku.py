
import numpy as np

def empty_rows(m):
    empty = []
    for row_index, row in enumerate(m):
         for col_index, value in enumerate(row):
              if value == 0:
                   empty.append((row_index,col_index))
    return empty

def row_check(m,n,coords):
    row = m[coords[0]]
    if n in row:
        return False
    return True

def col_check(m,n,coords):
    col = [row[coords[1]] for row in m]
    if n in col:
        return False
    return True

def grid_check(m,n,coords):
    x,y = coords
    s = matrix_separator(m,x,y)
    flattened = [val for row in s for val in row]
    if n in flattened:
        return False  
    return True

def matrix_separator(m,x,y):
    if x < 3:
        if y < 3:
            return [row[:3] for row in m[:3]]
        elif y < 6:
            return [row[3:6] for row in m[:3]]
        else:
            return [row[6:] for row in m[:3]]
    elif x < 6:
        if y < 3:
            return [row[:3] for row in m[3:6]]
        elif y < 6:
            return [row[3:6] for row in m[3:6]]
        else:
            return [row[6:] for row in m[3:6]]
    else:
        if y < 3:
            return [row[:3] for row in m[6:]]
        elif y < 6:
            return [row[3:6] for row in m[6:]]
        else:
            return [row[6:] for row in m[6:]]

def solve(m,empty):
    if not empty:  # Base case: no empty cells left
        return True  # Sudoku is solved
    
    coord = empty[0]  # Take the first empty cell
    row, col = coord  # Extract row and column indices
    
    for i in range(1, 10):  # Try numbers 1 to 9
        if grid_check(m, i, coord) and row_check(m, i, coord) and col_check(m, i, coord):
            m[row][col] = i  # Assign the number
            
            if solve(m, empty[1:]):  # Recursively solve for remaining empty cells
                return True
            
            m[row][col] = 0  # Backtrack if the solution is invalid
    
    return False  # No valid number found, puzzle is unsolvable at this state

def main():
    """Kindly read the Project overview before running this code
    But if you did skip it, go back and read it"""
    array = []
    """
    for i in range(9):
            row = input(f"Enter the values for row {i+1}: ")
            numbers = list(map(int, row.split()))
            array.append(numbers)
    """
    array = [
    [0, 3, 7, 0, 4, 0, 2, 0, 0],
    [2, 0, 6, 5, 0, 0, 0, 8, 0],
    [9, 0, 0, 0, 6, 0, 0, 0, 0],
    [4, 0, 8, 0, 3, 7, 0, 1, 5],
    [6, 0, 0, 1, 5, 8, 4, 0, 0],
    [0, 5, 0, 4, 2, 0, 0, 6, 0],
    [3, 8, 9, 7, 1, 6, 5, 0, 0],
    [1, 0, 4, 0, 8, 5, 0, 0, 3],
    [5, 6, 0, 3, 0, 0, 8, 7, 0],
]
    matrix = np.array(array)

    fill_m = empty_rows(matrix)
    solution = solve(matrix,fill_m)
    if solution:
        print("The solved sudoku puzzle is shown below: \n")
        print(matrix)
    else:
        print("This puzzle is unsolvable")

if __name__ == "__main__":
    main()
