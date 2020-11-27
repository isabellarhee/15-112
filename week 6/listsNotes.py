#lecture notes  LISTS
s = 'abc'
L = list(s) #immuatable
print(s)
print(L)

#creating lists
L = list() #empty list

#-------------recitation notes----------------
# .split() converts strings to lists
# you can cast a list to a strign by str(L)
#"".join(L)) concatenates strig  in L into 1 string (no delimter)
# can do " ".join(L) for a space in between the elements

#list comprehensions (set builder notation)
# optional, never actually HAVE to write these

#suppose we want to construct a list of the squares of integers
# 0 to 10 (exclusive)
#here is the normal way to do it
squaresA = []
for i in range(10):
    squaresA.append(i**2)

#here is w list comprehension
squaresB = [i**2 for i in range(10)]

#another example
evensA = [] 
for i in range(10):
    if i % 2 == 0
    evensA.append(i)

evensB = [i**2 for i in range(10) if i % 2 == 0]

#myList = [f(elem) for elem in g if p(elem)]

#do list CT with box and arrow method

a = [1,2,3]
b = a
b += [4] #does not break alias, changes a as well
b = b + [4] #breaks alias, b pointing to new, diff list