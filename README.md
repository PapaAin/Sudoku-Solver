# Sudoku-Solver

## Description
This project involves developing a Sudoku-solving application that takes an incomplete 9x9 Sudoku grid as input and determines the correct solution using backtracking and constraint satisfaction techniques.

## Features & Functionality:

-	Matrix Parsing: Reads a Sudoku puzzle as a NumPy array.
-	Empty Cell Detection: Identifies positions within the matrix that need to be filled.
-	Validation Checks: Ensures that each number (1-9) follows Sudoku rules:
  
    -	**Row Constraint**: No duplicate numbers within a row.

    -	**Column Constraint**: No duplicate numbers within a column.

    -	**Grid Constraint**: No duplicate numbers within a 3x3 sub-grid.

-	Recursive Solving: Implements a backtracking algorithm that systematically fills the puzzle while ensuring correctness.
-	User Input (Optional): Can accept Sudoku grids from manual user input.
-	Puzzle Validation: Determines if a given puzzle is solvable and prints the completed grid or returns an "unsolvable" message.
