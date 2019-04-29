#snippet1 prints space-separated row
my_list = [0,1,2,3,4,5,6,7,8,9]

assert( len(my_list) != 0 )

print(*my_list, sep=' ')
#-----------------------------------------------------------------------------------------------------------
print('snip1 output')#spacer
#snip2 prints space-separated column
my_list = [0,1,2,3,4,5,6,7,8,9]

assert( len(my_list) != 0 )

print(*my_list, sep='\n')
#------------------------------------------------------------------------------------------------------------
print('snip2 output')#spacer
#snip3 tries to display a 2dim array set up as a python list
coords = [ [1,2,3] , [4,5,6] , [7,8,9] ]
# however, snip3 actually prints 123456789 in a column, like snip2
for i in range( len(coords) ) :

    for j in range( len(coords[i]) ) :

        print(coords [i][j], end=' ')

        print()   # note this print is in scope of the j index and prints
                  # invis \n upon each pass through the inner, j loop
#------------------------------------------------------------------------------------------------------------
print('snip3 output')#spacer
#snip4 tries to display a 2dim array set up as a python list
coords = [ [1,2,3] , [4,5,6] , [7,8,9] ]
#however actually prints 1..9 in a space-sep row, like snip1
for i in range( len(coords) ) :
    for j in range( len(coords[i]) ) :  
        print(coords [i][j], end=' ')
print()  #  this print is in scope of the i index and prints
#           an invis \n upon each pass through the outer, i ,loop
#----------------------------------------------------------------------------------------------------------------
print('snip4 output')#spacer
#snip5 we can do better
matrix = [[1, 2, 3] , [ 4, 5, 6], [7, 8, 9]]

for row in matrix:
    for elem in row:
        
        print(elem, end=' ')
    print()
#----------------------------------------------------------------------------------------------------------------
print('snip5 output')#spacer
#snip6 can we strip out rows and columns?
for row in matrix:
    print(*row, end=' ')
#-----------------------------------------------------------------------------------------------------------------

print('snip6 output')#spacer
print()
#snip7 prints the rows but, yuck!
for row in matrix:
    print(row, sep=' ')

#------------------------------------------------------------------------------------------------------------------
print('snip7 output')
#snip8 better, prints each row (in a 'column fashion')
for row in matrix:
    print(*row, sep=' ')
#--------------------------------------------------------------------------------------------------------------------
print('snip8 output')
#snip9  print space-separated single row of matrix
print(*matrix[0], sep=' ')
print('snip9 output')
#------------------------------------------------------------------------------------------------------------------------
# how do we print the columns of this matrix? answer- transpose the rows, see (matrix transposition in python3)
# KISS, just want element[0] of each row, see SLICES

matrix = [[1, 2, 3] , [ 4, 5, 6], [7, 8, 9]]

#snip10 prints 1,4,7 i.e 'column 0' in column fashion
row = 0;
col = 0;
for row in range(0, len(matrix)):
   print(matrix[row][0], sep=' ')
   
#------------------------------------------------------------------------------------------------------------------------
print('snip10 output')   
#snip11  prints 2,5 8 i.e 'column1' in a column fashion
for i in range(0,len(matrix)):
    print(matrix[i][1], sep=' ')
#------------------------------------------------------------------------------------------------------------------------
print('snip11 output')
# snip12 prints 2,5,8 ==col1 in a 'row fashion'
row = 0;
col = 1;

for row in range(0,len(matrix)):
    print(matrix[row][col], end=' ')
#------------------------------------------------------------------------------------------------------------------------
print('snip12 output')
# so can now strip out any column
# snip13 strip out a column and load it into a new list

row = 0;
col = 1;
column = [];
   

for row in range(0,len(matrix)):
    column.append( matrix[row][col] )

print('column ' + str(col) +':', *column, sep=' ')
#-------------------------------------------------------------------------------------------------------------------------
print('snip13 output')
#-----------------------------------------------------------------------------------------------------------------------
# snip14
# try transpose the matrix
row = 0;
col = 0;
newrow = [];

for col in range(0,3):
    for row in range(0,len(matrix)):
        newrow.append( matrix[row][col] )
        
print(*newrow, sep=' ')
# nearly there
print('snip14 output')


# snip 15 try printing the leading diag and calc the trace





    
    
    
    
    






    
















