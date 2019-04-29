class Matrix(object):
    def __init__(self, matrix_string):
        
        self.matrix_string = matrix_string
        
        if len(self.matrix_string)==0:
            raise ValueError('empty string')
        
        # parse string into matrix ( of chars)
        self.matrix = [ list(segment.split()) for segment in matrix_string.split('\n') ]
        

    def row(self, index):               
        # convert row from a list of chars to a list of ints using map() iterator
        result = list( map( int, self.matrix[index-1]))  
        return result

    # extract column by extracting rowTranspose
    def column(self, index):
        
        result = list( zip(*self.matrix))[index-1]    #<-- zip obj not subscriptable, but tuple object is
        # convert tuple to a list so we can modify it
        result = list(result)
        # convert from a list of chars to a list of ints using map() iterator
        result = list (map(int, result))
        return result




#matrix = Matrix(matrix_string)
#index = 3
#print( matrix.row(index), sep =',')
#print(type(matrix.row(index)))                #<class 'list'> containing char types
#print()
#print( matrix.column(index), sep = ',')
#print (type( matrix.column(index)))        # <class 'tuple'> containing char types










