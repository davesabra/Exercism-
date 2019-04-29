class Matrix(object):
    def __init__(self, matrix_string):
        
        self.matrix_string = matrix_string
        
        if len(self.matrix_string)==0:
            raise ValueError('empty string')
        
    
        self.matrix = [ list(segment) for segment in matrix_string   #  parse string --> matrix 
                   .replace(' ','').split('\n') ]
        
        for row in self.matrix:
            print(*row, sep=' ')                                    #<-- test print                             
        
        self.matrix_transpose = list( zip(*self.matrix) )    # listify the zip generator                                      
        for row in self.matrix_transpose:
            print(*row, sep=' ')                                  # test build
                
    def rows(self):
        return self.matrix

    def columns(self):
        return self.matrix_transpose
    
    

#matrix_string = ''                   
#matrix_string = '1 2\n3 4'
#matrix_string = '1 2\n10 20'
#matrix_string = "1"
matrix_string = '1 2 3\n4 5 6\n7 8 9\n8 7 6'
#matrix_string = '89 1903 3\n18 3 1\n9 4 800'
#matrix_string = '1 2 3\n4 5 6\n7 8 9'
M = Matrix(matrix_string)
#print(*M.rows(), sep='\n') # prints the rows as they appear in the matrix
#print('Matrix rows-->'   , *M.rows(), sep=' ')  # print the rows in row fashion
for row in M.rows():
    print('Matrix row-->', *row, sep=' ')

for row in M.columns():
    print('Matrix column-->', *row, sep='\n')




