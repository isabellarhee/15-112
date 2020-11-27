#Sets and Dictionary notes
#s = set()
#set just like a list
#s.add(5)
#sets not subscriptable, not sorted, cant get ith value
#also no repeat elements
#{set elements}
#elements must be immutable
#very efficient

def isPermutation(L):
    #L is a permutation if it is the same as
    # [0, 1, 2, 3,....N]
    #NlogN steps
    #return sorted(L) == list(range(0,len(L)))
    #solve problem without sets^ but sorted is slow
    #better to take elements and put them in a set

    #4n steps
    return set(L) = set(list(range(len(L))))


#repeats
L = [1, 5, 4, 3, 7, 6]
def hasDuplicates(L):
    return len(L) > len(set(L))


#----------dictionary--------------- other language called MAP
#maps KEYS to VALUES
d = dict()
d['fred'] = 32
d['wilma'] = 28
#can search for KEY in dictionary
#dictionaries are just like sets lol, keys are a set, must be unique
#keys must be immutable 
#values can be anything
d = dict()
c = 'w'
d[c] = 0 #have to set to zero to do the +=
d[c] += 1
#don't know if key is already in dictionary
def letterCount(s):
    counts = dict()
    for ch in s.upper():
        if ((ch >= 'A') and (ch <= 'Z')):
            #now we want to add one to the count fopr
            #the letter ch
            counts[ch] = 1 + counts.get(ch, 0)
    return counts




#-------------recitation notes----------------
#sets unordered, no duplicates, immutable values
#set.get(key, default) avoids crashing if key doesnt exist
#can loop over dictionary keys, for k in d

'''
getPairSum(a, target) that takes a list of numbers and a target value
if there is a pair of #s that add up to target, return athat pair
otherwise return none
if more than one, return any of them

create a set w all elements of a: s = set(a)
loop through values
check if (target-curr element) in set
check if two numbers equal
    check if number appears more than once in original list
return None if we don't find a pair
'''

def getPairSum(a, target):
    s = set(a)
    for num1 in s:
        num2 = target - num1
        if (num2 in s):
            if (num1 != num2 or a.count(num2) > 1):
                return(num1, num2)
    return None


'''
invertDictionary(d) takes dictionary d that maps keys to values
and returns to values and returns dictionary of its inverse

create result dictionary, initially empty   
loop over each key-value pair
    check if value already a key in new dictionary
        add key to corresponding set
    else
        make new key value pair mapping value to {key}     
'''

def invertDictionary(d):
    result = dict()
    for key, val in d.items():
        result[val] = result.get(vall, set()) | {key}

    return result


'''
make empty result dictionary (will map movies to count)
loop through set
if this is the first time were seeing the mobie, initialize a count to 0
if weve seen it, our current count is in the dictionary
and add one to it
return that result dictionary
'''
def movieAwards(oscarResults):
    res = dict()
    for (award, movie) in oscarResult:
        res[movie] = res.get(movie, 0) + 1

    return res
