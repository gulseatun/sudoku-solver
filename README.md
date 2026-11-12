# Sudoku Solver

A Python command-line program that solves 9×9 Sudoku puzzles step by step using candidate elimination. Each placement is recorded with its row, column, and updated puzzle grid.

## Overview

This project was developed for **BBM103 – Introduction to Programming Laboratory I** at **Hacettepe University** (Fall 2023, Programming Assignment 2).

The solver finds candidate numbers for each empty cell by checking its row, column, and 3×3 subgrid. When a cell has exactly one valid candidate, the program fills it and repeats the process. The original implementation uses recursion to continue after each placement. **It does not use backtracking**; it is intended for puzzles that can be completed through single-candidate elimination, as specified in the assignment.

## Features

- Reads a 9×9 puzzle from a plain-text file, using `0` for empty cells.
- Identifies a valid number when a cell has exactly one candidate.
- Writes a step-by-step solution to a user-specified text file.
- Shows the chosen value, row, column, and updated board at every step.
- Uses only the Python standard library.

## Requirements

Python 3 (original assignment environment: Python 3.6.8). No third-party packages are required.

## Usage

From the repository root, run:

```bash
python sudoku.py examples/i1.txt solution.txt
```

On systems where Python 3 is invoked as `python3`:

```bash
python3 sudoku.py examples/i1.txt solution.txt
```

The command takes two positional arguments: an input puzzle path and an output file path. The output file is created or overwritten.

## Input format

The input contains nine lines with nine space-separated digits per line. A `0` represents an empty cell. For instance, the first row of `examples/i1.txt` is:

```text
0 2 5 0 0 7 0 0 4
```

## Output format

The output includes the placement and the board after each step:

```text
------------------
Step 1 - 3 @ R2C7
------------------
0 2 5 0 0 7 0 0 4
0 0 1 0 0 5 3 2 0
7 0 0 0 2 0 5 0 0
5 0 9 0 0 4 8 0 0
0 0 0 0 0 0 0 0 0
0 0 7 5 0 0 6 0 9
0 0 3 0 7 0 0 0 6
0 4 0 1 0 0 7 0 0
8 0 0 2 0 0 9 1 0
------------------
```

## Examples and verification

The `examples/` directory contains **10 provided input files** (`i1.txt`–`i10.txt`) and their corresponding expected outputs (`o1.txt`–`o10.txt`). The original `sudoku.py` was run with all ten inputs; the generated step sequences and puzzle states matched the provided outputs. There is one formatting-only difference: the generated output ends with a newline while the provided reference outputs do not.

## Notes

This repository preserves the original coursework source code without refactoring. The implementation assumes the input follows the assignment's nine-row, space-separated format and does not provide a general-purpose solver for puzzles requiring guesses or backtracking.
