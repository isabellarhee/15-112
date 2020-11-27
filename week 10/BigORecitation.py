#big O notes from recitation

#big O
'''
relationship between the size of the input(s) and the time it takes to run
you don't include constants or lower order terms

big rules:
    ignore constants
            O(n**2 - 6n*logn + log_2 3n) = O(n**2)
            O(3**n) = O(2**n)
            why? asymptomatic behavior
if you do W work in a loop that runs L time, efficiency is W*L
    O(n) work inside of a loop that runs 26 tiems --> O(n)
    O(log n) work inside of a loop that runs n time --> O(n logn)

if you do actions sequencially, just add them
    an if statement is O(n**2) and code inside is O(n) --> O(n**2)

when thinking about builtin functions efficiencies, think about
how it's implemented
    work of L.pop() depends on how many elements need to have 
    their efficiencies shifted, if its a constant number
    then its O(1) if the number is related to n then its O(n)

    L.count(N) is O(n) because it has to loop over all n elements of L

Set & dictionaries = God Tier
    adding an element / key-value pair: o(1)
    checking membership / extracting value: O(1)

the classes we usually talk about: can we think of examples for each of them


'''

#contains pythagorean triple
'''
takes list of positive integers and returns true if there are 3 values
that create a pythagorean triple

must be faster than O(N**3)

O(n^3):
3 nested for loops for all possible combinations

faster solution:
cast list to a set
instead of looping a third time, calculate what the third number
needs to be and check if its in the set

'''

def containsPythagoreanTriple(L):
    setL = set(L)  #O(n)
    for num1 in L: #O(n)
        for num2 in L:  #O(n)
            num3 = (num1**2 + num2**2)**.5  #O(1)
            if (num3 in setL):  #O(n)
                return True      #O(n)
    return False  #overall O(n^2)

'''
Mr. Krabs problem

check all the logs of time <= t, if even then the person is not in the room


use a dictionary mapping each name to a boolean indicating
if they are in the room
we can figure out if a person was in the room at time t by looking
up in the dictionary
    if so add them to result set
'''

def inRoomAtTime(logs, t): #O(n) overall
    timeDict = {}
    resultSet = set()
    for time,name in logs:  #O(n)
        if time > t:  #O(1)
            break
        if name not in timeDict: #O(1)
            timeDict[name] = True
        else:
            timeDict[name] = not timeDict[name]
    #generate the time dictionary
    for name in timeDict: #O(n)
        if timeDict[name]:  #O(1)
            resultSet.add(name)
    return resultSet

def getTimeSpent(logs):
    '''
    If there was only 1 person:
    take the difference of when the enter and exit, then add that to total
        even index is entering
        odd index is leaving
    get each persons list of times
        loop through the list of tuples
        if name isn't in dictionary, add that name to the dictionary
        if the name is in dictionary, add new tuple to existing list
    '''
    times = dict()
    for (time, name) in logs:
        if name in times:
            times[name].append(time)
        else:
            times[name] = [time]

    result = dict()
    for person in times:
        totalTime = 0
        timeList = times[person]
        for i in range(0, len(timeList), 2):
            totalTime += timeList[i+1]-timeList[i]
        result[person] = totalTime
    return result
    

#---------------------------------------
#linear search vs binary search

def linearSearch(L, x):
    for i in range(len(L)):
        if L[i] == x:
            return True
    return False

#overall big-o O(n)

def binarySearch(L, x):
    lo = 0
    hi = len(L)
    while lo < hi:  #worst case log(n)
        mid = (lo + hi) // 2
        if L[mid] == x:
            return True
        elif L[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return False

# 2^10 = 1024
