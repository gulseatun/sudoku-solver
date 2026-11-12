import sys


def finding_row(row, sudoku): #This function determines and returns the numbers that does not exist in the specified row.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row_elements = []
    for i in range(9):
        row_elements.append(sudoku[row][i])

    row_possibility = []
    for element in numbers:
        if not element in row_elements: 
            row_possibility.append(element)

    return(row_possibility)


def finding_column(column, sudoku): #This function determines and returns the numbers that does not exist in the specified column.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    column_elements = []
    for i in range(9):
        column_elements.append(sudoku[i][column])

    column_possibility = []
    for element in numbers:
        if not element in column_elements:
            column_possibility.append(element)

    return(column_possibility)



#This function firstly creates a sub grid elements list according to specified number's place.
#Then it determines and returns the numbers that does not exist in the specified number's sub grid.
def finding_square(row, column, sudoku): 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    square_elements = []
    if row % 3 == 0:
        if column % 3 == 0:
            for i in range(row, row+3):
                for j in range(column, column+3):
                    square_elements.append(sudoku[i][j])

        if column % 3 == 1:
            for i in range(row, row+3):
                for j in range(column-1, column+2):
                    square_elements.append(sudoku[i][j])

        if column % 3 == 2:
            for i in range(row, row+3):
                for j in range(column-2, column+1):
                    square_elements.append(sudoku[i][j])

    if row % 3 == 1:
        if column % 3 == 0:
            for i in range(row-1, row+2):
                for j in range(column, column+3):
                    square_elements.append(sudoku[i][j])

        if column % 3 == 1:
            for i in range(row-1, row+2):
                for j in range(column-1, column+2):
                    square_elements.append(sudoku[i][j])

        if column % 3 == 2:
            for i in range(row-1, row+2):
                for j in range(column-2, column+1):
                    square_elements.append(sudoku[i][j])


    if row % 3 == 2:
        if column % 3 == 0:
            for i in range(row-2, row+1):
                for j in range(column, column+3):
                    square_elements.append(sudoku[i][j])

        if column % 3 == 1:
            for i in range(row-2, row+1):
                for j in range(column-1, column+2):
                    square_elements.append(sudoku[i][j])

        if column % 3 == 2:
            for i in range(row-2, row+1):
                for j in range(column-2, column+1):
                    square_elements.append(sudoku[i][j])


    square_possibility = []
    for element in numbers:
        if not element in square_elements:
            square_possibility.append(element) 

    return(square_possibility)   


def print_sudoku(sudoku): #This function coverts sudoku step to string format and returns it. 
    sudoku_str = ""
    for i in sudoku:
        for index, j in enumerate(i):
            sudoku_str += str(j) 
            if index != 8 :
                sudoku_str += " " 
        sudoku_str += "\n"

    return sudoku_str



#This function checks matches in numbers that can be placed to the cell according to the row, column and sub grid. 
#If there is only one possibility the function places it and prints the step to the file.
def finding_matches(row, column, sudoku, step): 
    matches = list(set(finding_row(row, sudoku)) & set(finding_column(column, sudoku)) & set(finding_square(row, column, sudoku)))
    if len(matches) == 1:
        
        sudoku[row][column] = matches[0]

        output_writer = open(output_sudoku, "a")
        output_writer.write("Step {} - {} @ R{}C{}\n".format(step, matches[0], row+1, column+1) +  "------------------\n" + print_sudoku(sudoku) + "------------------\n")
        output_writer.close()
        return True

    else:
        return False
    

#This function uses finding_matches function to determine if there is a match. 
#If there is a match, it looks if there are any zeros and calls the function recursively if there is. 
#When there are no zeros left it exists.
def sudoku_solve(sudoku, step): 

    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:

                if not finding_matches(row, column, sudoku, step):
                    continue
                    
                elif any(0 in i for i in sudoku): 
                    sudoku_solve(sudoku, step+1)
                    
                else:
                    exit()

if __name__ == "__main__":

    input_sudoku = sys.argv[1]
    output_sudoku = sys.argv[2]

    input_sudoku_read = (open(input_sudoku, "r")).read() #Reading input

    sudoku = []  
    for index in range(0,145,18):  #Getting rows as list elements and integers
            sudoku.append([int(input_sudoku_read[i]) for i in range(index, index+17, 2)] )

    output_writer = open(output_sudoku, "w")
    output_writer.write("------------------\n") #This part prints the first dash lines because it should only occur in the beggining of the file.
    output_writer.close() #Closing file to avoid overwrite.
    sudoku_solve(sudoku, 1)


   


                





