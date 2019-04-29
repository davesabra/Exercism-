#matrix_string = '1 2\n3 4'
#matrix_string = '1 2 3\n4 5 6\n7 8 9'
#matrix_string = '89 1903 3\n18 3 1\n9 4 800'
matrix_string = "1 2 3\n4 5 6\n7 8 9\n8 7 6"

# parse matrix_string into matrix
rows = []
matrix = []
rowctr = 0
for _ in matrix_string.replace(" ", "").split('\n'):
    rowctr += 1
    rows = _.split()
    print('row-->', *rows)                    # code check

# output looks right but have we built a matrix really or just printed 4 individual rows?

    
#matrix = [[str(char) for char in line] for line in matrix_string.splitlines('\n')]
#matrix = [[list(line)] for line in matrix_string.splitlines('\n')]
#[[x for x in line] for line in matrix_string.split('\n')]
matrix = [ list(line) for line in matrix_string.replace(" ", "").split('\n') ]

print(*matrix, sep=' ')                      # built matrix
matrix_T = zip(*matrix)                      # transpose matrix
print(*matrix_T, sep=' ')                    # code check


# In Python 3, map returns an iterator, so to get a list from the last
# solution you need list(map(list, zip(*lis))) or [*map(list, zip(*lis))]. 

#You can use zip with * to get transpose of a matrix:
# (rather than importing a whole library(inelegant) and output is a numpy array, longer, slower)

#A = [[ 1, 2, 3],[ 4, 5, 6]]
#print(A)
#A = zip(*A)
#print(A)
#[(1, 4), (2, 5), (3, 6)]
#>>> lis  = [[1,2,3], 
#... [4,5,6],
#... [7,8,9]]
#>>> zip(*lis)
#[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
#If you want the returned list to be a list of lists:

#>>> [list(x) for x in zip(*lis)]
#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#or
#>>> map(list, zip(*lis))
#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]



    





   
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