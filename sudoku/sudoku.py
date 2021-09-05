# EDIT THE FILE WITH YOUR SOLUTION
import re, os
from pdflatex import PDFLaTeX

class Sudoku:

    # constructor
    def __init__(self, file):
        self.file = file
        self.clean_data()
                
    def validate_row(self, row, grid):
        temp = grid[row]
        # Removing 0's.
        temp = list(filter(lambda a: a != 0, temp))
        # Checking for invalid values.
        if any(i < 0 and i > 9 for i in temp):
            print("Invalid value")
            return -1
        # Checking for repeated values.
        elif len(temp) != len(set(temp)):
            return 0
        else:
            return 1
        
    def validate_col(self, col, grid):
        # Extracting the column.
        temp = [row[col] for row in grid]
        # Removing 0's. 
        temp = list(filter(lambda a: a != 0, temp))
        # Checking for invalid values.
        if any(i < 0 and i > 9 for i in temp):
            print("Invalid value")
            return -1
        # Checking for repeated values.
        elif len(temp) != len(set(temp)):
            return 0
        else:
            return 1
        
    def validate_subsquares(self, grid):
        for row in range(0, 9, 3):
            for col in range(0,9,3):
                temp = []
                for r in range(row,row+3):
                    for c in range(col, col+3):
                        if grid[r][c] != 0:
                            temp.append(grid[r][c])
                # Checking for invalid values.
                if any(i < 0 and i > 9 for i in temp):
                    print("Invalid value")
                    return -1
                # Checking for repeated values.
                elif len(temp) != len(set(temp)):
                    return 0
        return 1
        
    def clean_data(self):
        sudoku_board = []
        x=[]
        
        openFile = open(self.file, "r")
        sudokuPuzzle = openFile.readlines()

        for line in range(len(sudokuPuzzle)):
            if line != len(sudokuPuzzle) - 1:
                sudokuPuzzle[line] = re.sub(r'\n', '',sudokuPuzzle[line])
                spaceRm_1 = sudokuPuzzle[line].strip() # remove trailing and leading space
                x.append(spaceRm_1)
            else:
                sudokuPuzzle[line] = re.sub(r'\n', '',sudokuPuzzle[line])
                spaceRm_1 = sudokuPuzzle[line].strip()
                x.append(spaceRm_1)
                      
        spaceRm_2 = [row for row in x if len(row) > 0] # remove rows with space
        
        counter=0
        for i in spaceRm_2:
            for x in i: # check for space in-btw
                if x.isspace():
                    counter += 1
            
            if counter > 0:
                spaceRm_3 = i.replace("  ", " ") # minimize space in-btw to 1
                if self.file.startswith("sudoku_wrong"):
                    print('SudokuError: Incorrect input')
                    return
                else:
                    sudoku_board.append(list(map(int,spaceRm_3.split(" "))))            
            else:
                lists = list(i)
                for i in range(0, len(lists)): # convert list strings to int
                    lists[i] = int(lists[i])
                sudoku_board.append((lists))

        openFile.close()
        return sudoku_board
    
    # Function to check if the board invalid.
    def validate_board(self, grid):
        # Check each row and column.
        for i in range(9):
            res1 = self.validate_row(i, grid)
            res2 = self.validate_col(i, grid)
            # If a row or column is invalid then the board is invalid.
            if (res1 < 1 or res2 < 1):
                print("There is clearly no solution.")
                return
        # If the rows and columns are valid then check the subsquares.
        res3 = self.validate_subsquares(grid)
        if (res3 < 1):
            print("There is clearly no solution.")
        else:
            print("There might be a solution")
    
    
    def preassess(self):
        
        sudoku_board=self.clean_data()
        
        return self.validate_board(sudoku_board)
   

    def bare_tex_output(self):
        
        sudoku_board = self.clean_data()
        get_file_name = os.path.splitext(self.file)[0]
        get_file_no = get_file_name.split('_')
        
        with open('sol_sudoku_'+get_file_no[1]+'_bare.tex','r') as sudo:
            sudo = sudo.read()
            
            for i in sudoku_board:
                new_sudo = sudo.replace('$sol_sudoku_'+get_file_no[1]+'_bare.tex$', str(sudoku_board))

            with open('sudoku_'+get_file_no[1]+'_bare.tex', 'w') as new_output:
                new_output.write(new_sudo)

        pdfl = PDFLaTeX.from_texfile('sudoku_'+get_file_no[1]+'_bare.tex')
        pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
    
    
    def forced_tex_output(self):
        
        sudoku_board = self.clean_data()
        get_file_name = os.path.splitext(self.file)[0]
        get_file_no = get_file_name.split('_')
        
        with open('sol_sudoku_'+get_file_no[1]+'_forced.tex','r') as sudo:
            sudo = sudo.read()
            
            for i in sudoku_board:
                new_sudo = sudo.replace('$sol_sudoku_'+get_file_no[1]+'_forced.tex$', str(sudoku_board))

            with open('sudoku_'+get_file_no[1]+'_forced.tex', 'w') as new_output:
                new_output.write(new_sudo)

        pdfl = PDFLaTeX.from_texfile('sudoku_'+get_file_no[1]+'_forced.tex')
        pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
        
    
    def marked_tex_output(self):
        
        sudoku_board = self.clean_data()
        get_file_name = os.path.splitext(self.file)[0]
        get_file_no = get_file_name.split('_')
        
        with open('sol_sudoku_'+get_file_no[1]+'_marked.tex','r') as sudo:
            sudo = sudo.read()
            
            for i in sudoku_board:
                new_sudo = sudo.replace('$sol_sudoku_'+get_file_no[1]+'_marked.tex$', str(sudoku_board))

            with open('sudoku_'+get_file_no[1]+'_marked.tex', 'w') as new_output:
                new_output.write(new_sudo)

        pdfl = PDFLaTeX.from_texfile('sudoku_'+get_file_no[1]+'_marked.tex')
        pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
        
    
    def worked_tex_output(self):
        
        sudoku_board = self.clean_data()
        get_file_name = os.path.splitext(self.file)[0]
        get_file_no = get_file_name.split('_')
        
        with open('sol_sudoku_'+get_file_no[1]+'_worked.tex','r') as sudo:
            sudo = sudo.read()
            
            for i in sudoku_board:
                new_sudo = sudo.replace('$sol_sudoku_'+get_file_no[1]+'_worked.tex$', str(sudoku_board))

            with open('sudoku_'+get_file_no[1]+'_worked.tex', 'w') as new_output:
                new_output.write(new_sudo)

        pdfl = PDFLaTeX.from_texfile('sudoku_'+get_file_no[1]+'_worked.tex')
        pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
    
    
    
# getFile = input('Enter Name of File: ')
sudoku = Sudoku('sudoku_1.txt')
sudoku.preassess()
# sudoku.bare_tex_output()
# sudoku.forced_tex_output()
# sudoku.marked_tex_output()
# sudoku.worked_tex_output()