#import numpy as np

#matrix_string = '1 2\n3 4'
#matrix_string = '1 2 3\n4 5 6\n7 8 9'
#matrix_string = '89 1903 3\n18 3 1\n9 4 800'
matrix_string = "1 2 3\n4 5 6\n7 8 9\n8 7 6"

# parse matrix_string into rows
rows = []
matrix = []
rowctr = 0
for _ in matrix_string.split('\n'):
    rowctr += 1
    rows = _.split()
    matrix = [ rows  ]
    print('row-->', *rows)                    # code check
    print(*matrix, sep='\n')
    
for row in matrix:
    for val in row:
        print(val) 
    





   
# use rows to build matrix of size rowlength x number of rows(columnlength)     
# n = len(rows)
# m = rowctr
# matrix = [ [ 0 for i in range(n) ] for j in range(m) ]
# print(*matrix, sep='\n')                                    #code check






    
#def transpose(matrix):
#    return [[matrix[i][j] for i in range(len(matrix[j]))] for j in range(len(matrix))]


#transpose(matrix)
#matrix = numpy.matrix(matrix)
# matrix.T 