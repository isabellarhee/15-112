def sunTo(n):
    sum = 0
    #da counter in range -> first # inclusive, last # exclusive
    for counter in range(1,n+1): #add third ,n at end for "step"
        print(counter)
        sum += counter
    return sum

print(sumTo(3))
print(1 + 2 + 3)

def sumOfSquaresTo(n):
    total = 0
    for counter in range(1, n+1):
        total += counter ** 2
    return total

print("answer: ", sumOfSquaresTo(3))

def sumOfOddSquaresTo(n):
    total = 0
    for counter in range(1, n+1): #range(1 , n+1, 2)
        if (counter % 2 ==1): #this can be done with the step^
            total += counter ** 2
    return total

print("answer: ", sumOfOddSquaresTo(3))


#while loops--------------------------

def getLeftMostDigit(n):
    while (n >= 10):
        n //= 10
    return n

print(getLeftMostDigit(78234872))

def isPrime(n):
    if(n < 2):
        return False
    for counter in range(2, n):
        if (n % counter == 0):
            #the counter is a factor of n, n not prime
            return False
        
    return True

def nthPrime(n):
    #2, 3, 5, 7 ,13  (n)
    found = 0
    counter = 0
    while (found <= n ):
        counter += 1
        if (isPrime(counter)):
            found +=1
    return counter

    