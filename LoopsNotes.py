#loops

#for loop
# A for loop repeats an action a specific number of times
# based on the provided range
def sumFromMToN(m, n):
    total = 0
    # note that range(x, y) includes x but excludes y
    for x in range(m, n+1):
        total += x
    return total
#dont need a loop for
def sumFromMToN(m, n):
    return sum(range(m, n+1))

#if you dont set first parameter, defaults set the starting number to 0
def sumEveryKthFromMToN(m, n, k):
    total = 0
    # the third parameter becomes a step
    for x in range(m, n+1, k):
        total += x
    return total
# Here we will range in reverse
# (not wise in this case, but instructional)
def sumOfOddsFromMToN(m, n):
    total = 0
    for x in range(n, m-1, -1):
        if (x % 2 == 1):
            total += x
    return total

# We can put loops inside of loops to repeat actions at multiple levels
# This prints the coordinates
def printCoordinates(xMax, yMax):
    for x in range(xMax+1):
        for y in range(yMax+1):
            print("(", x, ",", y, ")  ", end="")
        print()


#while loops
# use while loops when there is an indeterminate number of iterations

def leftmostDigit(n):
    n = abs(n)
    while (n >= 10):
        n = n//10
    return n

# continue, break, and pass are three keywords used in loops
# in order to change the program flow
for n in range(200):
    if (n % 3 == 0):
        continue # skips rest of this pass
    elif (n == 8):
        break # skips rest of entire loop
    else:
        pass # does nothing! pass is a placeholder, not needed here
    print(n, end=" ")
print()

def isPrime(n):
    if(n < 2):
        return False
    for counter in range(2, n):
        if (n % counter == 0):
            #the counter is a factor of n, n not prime
            return False
        
    return True

# Note: this is still not the fastest way, but it's a nice improvement.
def fasterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = roundHalfUp(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def nthPrime(n):
    #2, 3, 5, 7 ,13  (n ==3)
    found = 0
    counter = 0
    while (found <= n ):
        counter += 1
        if (isPrime(counter)):
            found +=1
    return counter

def sumOfDigits(n):
    n = abs(n)
    result = 0
    while (n > 0):
        d = n % 10
        n //= 10
        result += d
    return result

def isAdditivePrime(n):
    return isPrime(n) and isPrime(sumOfDigits(n))

def nthAdditivePrime(n):
    
    found = 0
    counter = 0
    while (found <= n ):
        counter += 1
        if (isAdditivePrime(counter)):
            found +=1
    return counter



#------------------------Recitation Notes-----------------
#n % 2 == 1 we know it's odd
#this function takes an int and returns the oddest digit
#use helper function to count a specific digit
#loop through the odd digits and call our helper
#count 1s 3s 5s 7s 9s
#bestNum keeps track of oddest so far --> compare with currNum

#count occurences of digit k in n
def digitCount(n):
    n = abs(n)
    digits = 0
    temp = n
    
    while (temp > 0):
        digits+=1
        temp //=10


def countDigit(n,k):
    n = abs(n)
    count = 0
    while (n > 0):
        currDigit = n % 10
        if(currDigit ==k): count +=1

    return count

    


def oddestDigit(n):
    bestDigit = 0
    for i in range(1,10,2):
        currCount = countDigit(n,currDigit)
        if (currCount >= bestCount and currCount != 0):
            bestCount = currCount
            bestDigit = currDigit
    return bestDigit


#nearly square O.o
#to find if a number is nearly square, remove zeros
#check if it is a perfect square
#check to see if any number in the interval n-10 to n+10 is squarish


def removeZeros(n):
    newN = 0
    power = 0
    while n > 0:
        digit = n % 10
        if digit != 0:
            newN += digit * (10 ** power)
            power +=1
        n //= 10
    return newN

def isPerfectSquare(n):
    return int(n ** .5) == n ** 0.5

def isNearlySquarish(n):
    for i in range(n - 10, n+11):
        if isPerfectSquare(removeZeros(i)):
            return True
    
    return False

#NTH FUNCTION TEMPLATE!!!!! SAVE FOR LATER
def nthNearlySquarish(n):
    found = 0
    guess = 0
    while found <= n:
        guess +=1
        if isNearlySquarish(guess):
            found += 1

    return guess

#-----------------LEcture Notes---------------------------------------------------
#continue -> like break but doesn't end the loop
#ex
for n in range(200):
    if ( n % 3 == 0):
        continue #skips rest of this pass
    elif (n == 8):
        break #skips rest of the entire loop
    else:
        pass #does nothing pass is a placeholder
    print(n, end="")
print()


#IDK if i already had this
# Note- this is advanced content, as it uses strings. It's okay
# to not fully understand the content below.
def readUntilDone():
    linesEntered = 0
    while (True):
        response = input("Enter a string (or 'done' to quit): ")
        if (response == "done"):
            break
        print("  You entered: ", response)
        linesEntered += 1
    print("Bye!")
    return linesEntered

linesEntered = readUntilDone()
print("You entered", linesEntered, "lines (not counting 'done').")

### COMMAND - SHIFT - C to end the terminal if stuck in infinite loop


def truncateLeft(n):
    #9137 --> 137  
    #29137 % 10**3 == 137
    return (n % (10**digitCount(n)-1))

def nthLeftTruncatablePrime(n):
    if (n < 2):
        return False
    while (n > 0):
        if (not isPrime(n)):
            return False
        truncateLeft(n)  #removeLeftmostDigit(n)
    return True

def mostFrequentDigit(n):
    bestDigit = None
    bestCount = 0
    for counter in range(10):
        count = digitCount() #but for a specific digit
        if(count > bestCount):
            bestCount = count
            bestDigit = digit
    return bestDigit