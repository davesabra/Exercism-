class Matrix(object):

    def __init__(self, matrix_string):
        
        self.matrix_string = matrix_string
        
        if len(self.matrix_string)==0:
            raise ValueError('empty string')
        
        # parses matrix_string into an int matrix
        self.matrix = [[int(i) for i in segment.split()]
            for segment in matrix_string.split('\n')]
        
    
    def row(self, index):
        return  self.matrix [index-1]    

    def column(self, index):
        number_of_cols = len(self.matrix[0]) # get row dimension   
        return [[row[i] for row in self.matrix]
                   for i in range(number_of_cols)] [index-1]

