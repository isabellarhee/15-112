#lecture notes on recursion
def sumToN(n):
    return sum(range(n+1))

def factorial(n):
    result = 1
    for v in range(1, n+1):
        result *= v
    return result
    
def factorialRecursive(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)

'''
def f(n):
    if (in base case):
        return something not recursive
    else:
        return an answer that recurses on a smaller thing

'''

def listSum(L):
    if (L == [ ]):
        return 0
    else:
        first = L[0]
        rest = L[1:]
        return first + listSum(rest) 

def listSum(L):
    if len(L) == 0:
        return 0 
    elif (len(L) == 1):
        return L[0]
    else:
        mid = len(L) // 2
        return listSum(L[:mid]) + listSum(L[mid:])

def power(a,b):
    #returns a**b
    if (b == 0):
        return 1
    else:
        return a * power(a, b-1)

#1,1,2,3,5,8,13,21,34....
def fib(n)  #wrapper function
    #no for loops or while loops allowed
    return fib1(n, 0)


def fib1(n, depth):
    print(" "*depth, f'fib({n})')
    if (n == 0) or (n == 1):
        result = 1
    else:
        result fib1(n-1, depth+1) + fib1(n-2, depth+1)
    print(" "*depth, "-->",result)
    return result

#---------------------------------------
#recitation notes

def longestStrippedLine(s):
    '''
    takes multiline string and returns longest stripped line
    splitlines, loop thru lines, get rid of leading spaces
    track greatest length
    make a helper function
    '''
    L = s.splitlines()
    return longestStrippedLineHelper(L, 0)

def longestStrippedLineHelper(s, longestLine):
    if L == []:
        return longestLine
    else:
        line = L[0].strip()
        if (len(line) > len(longestLine:
            longestStrippedLineHelper(L[1:], line)
        else:
            longestStrippedLineHelper(L[1:], longestLine)

def flatten(L):
    '''
    takes list (which may contain lists)

    '''
    if L == []:
        return []
    elif not isinstance(L, list):
        return [L]
    else:
        return flatten(L[0]) + flatten(L[1:])

#------------------------------------------
#lec part 2
#folder is a recursive data structure
#print everything in a folder, if its a file, print it,
#if its a folder, go into it

import os
def printFiles(path):
    # Base Case: a file. Just print the path name.
    #os.path.getsize(path) == 0:
    #   print(path) #crashes so dont use this

    if os.path.isfile(path):
        print(path)
    else:
        # Recursive Case: a folder. Iterate through its files and folders.
        files = os.listdir(path)
        printFilesInAGivenFolder(path, files)
        

def printFilesInAGivenFolder(path, files):
    if len(files) == 0:
        pass
    else:
        firstFile = files[0]
        restOfFiles = files[1:]
        printFiles(path + '/' + firstFile)
        printFilesInAGivenFolder(path, restOfFiles)

printFiles('sampleFiles')
#os.listdir('.')
#os.listdir('sampleFiles')
#returns a list of names of files that live inside that dir

# Note: if you see .DS_Store files in the sampleFiles folders, or in the
# output of your function (as often happens with Macs, in particular),
# don't worry: this is just a metadata file and can be safely ignored.

import os
def removeTempFiles(path, suffix='.DS_Store'):
    if path.endswith(suffix):
        print(f'Removing file: {path}')
        os.remove(path)
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            removeTempFiles(path + '/' + filename, suffix) #to get path

removeTempFiles('sampleFiles')
# removeTempFiles('sampleFiles', '.txt') # be careful

import os
def listFiles(path):
    if os.path.isfile(path):
        # Base Case: return a list of just this file
        return [ path ]
    else:
        # Recursive Case: create a list of all the recursive results from
        # all the folders and files in this folder
        files = [ ]
        for filename in os.listdir(path):
            files += listFiles(path + '/' + filename)
        return files

print(listFiles('sampleFiles'))
#function should return the same type no matter where returning from

#-------------fractals---------------
from cmu_112_graphics import *

class MyFractalApp(App):
    def appStarted(self):
        self.level = 1

    def drawFractal(self, canvas, level, otherParams):
        if level == 0:
            pass # base case
        else:
            pass # recursive case; call drawFractal as needed with level-1

    def keyPressed(self, event):
        if event.key in ['Up', 'Right']:
            self.level += 1
        elif (event.key in ['Down', 'Left']) and (self.level > 0):
            self.level -= 1

    def redrawAll(self, canvas):
        margin = min(self.width, self.height)//10
        otherParams = None
        self.drawFractal(canvas, self.level, otherParams)
        canvas.create_text(self.width/2, 0,
                           text = f'Level {self.level} Fractal',
                           font = 'Arial ' + str(int(margin/3)) + ' bold',
                           anchor='n')
        canvas.create_text(self.width/2, margin,
                           text = 'Use arrows to change level',
                           font = 'Arial ' + str(int(margin/4)),
                           anchor='s')
        canvas.create_text(self.width/2, self.height/2,
                           text = 'Replace this with your fractal',
                           font = 'Arial 24 bold')

MyFractalApp(width=400, height=400)

#-----------recitation notes-------------------
#is prime but recursive

def isPrime(n):
    if n < 2:
        return False
    return isPrimeHelper(n, 2)

def isPrimeHelper(n, i):
    if n == i:
        return True
    else:
        if n % i == 0:
            return False
        return isPrimeHelper(n, i+1)

def reverse(L):
    if L == []:
        return []
    else:
        return reverse(L[1:] + [L[0]])

def reverse2(L):
    if L == []:
        return []
    if len(L) == 1:
        return L
    left = L[:len(L)//2]
    right = L[len(L)//2:]
    return reverse2(right) + reverse(left)