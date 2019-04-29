class Matrix(object):
    def __init__(self, matrix_string):
        
        self.matrix_string = matrix_string
        
        if len(self.matrix_string)==0:
            raise ValueError('empty string')
        
        # parse the string into rows by split()ing at newlines
        for _ in matrix_string.split('\n'):
            _.split()
            print(_)                               #logic check, print matrix
        
        print() #spacer
        # rebuild the string as an rows x columns matrix
        #self.rows    = []
        #self.columns = []
        
        # builds rows
        #self.rows = [_.split() for _ in matrix_string.split('\n')  ]
        
        
        # alternatively, parse matrix_string and build rows
        # self.rows = []
        for _ in matrix_string.split('\n'):
            #self.rows = _.split()
            print('row-->', _)               #logic check, print rows
            
            
        # now build matrix from rows
        matrix = [ list(line) for line in matrix_string.replace(" ", "").split('\n') ]
        #print(*matrix, sep=' ')                       # code check
        
        print() #spacer
        
        matrix_T = zip(*matrix)                      # transpose matrix
        #print(*matrix_T, sep=' ')                    # code check
        
        # print the rows of the transposed matrix
        for row in matrix_T:
            print('col-->', *row, sep=' ')
        
        

    
# put display functions into these containers:    
    
    def row(self, index):
        pass
        #self.index = index
        #print('row-->', index, self.rows[index-1])

    def column(self, index):
        pass


#test data
#matrix_string = ''                    #empty   
#matrix_string = '1 2\n3 4'
#matrix_string = '1 2\n10 20'
#matrix_string = "1"
matrix_string = "1 2 3\n4 5 6\n7 8 9\n8 7 6"
#matrix_string = '89 1903 3\n18 3 1\n9 4 800'
#matrix_string = '1 2 3\n4 5 6\n7 8 9'
Matrix(matrix_string)

