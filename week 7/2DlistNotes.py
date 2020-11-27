#-------lecture notes-----------------------




#2d lists
rows = 2
cols = 5
l = [[0] * cols] * rows

#---------recitation notes---------------------
#calcSum
''''
take  2d list and return sum of all numbers

nested for loops
check type of value, append to a new list if it's an int or float

'''
def calcSum(L):
    total = 0
    for row in L:
        for item in row:
            if (type(item) == int or type(item) == float):
                total += item
            
    return total

'''write a function that takes rectangular 2d list of ints
and returns true if L is foiled. aka every row in Lis equal to
some column in L
example
[[1,1,2],
[2,1,1],
[1,2,1]]

-generate a list of columns -> generate TRANSPOSE of L
-loop through rows
-check if each row is in transpose
'''
def isFoiled(L):
    transpose = []
    #make the transpose here
    for c in range(len(L[0]):
        col = []
        for row in L:
            col.append(row[c])
        transpose.append(col)
            

    for row in L:
        if i not in transpose:
            return False

    return True

'''
remove row and col
take a 2d list and a row number and a col number
remove specified row and col

'''
def removeRowandCol(L, row , col):
    out = []
    for r in range(len(L)):
        if r != row:
            out.append(L[r][:col]+L[r][col+1:])

    return out