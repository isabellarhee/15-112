#################################################
# hw8.py
#
# Your name:  Isabella Rhee
# Your andrew id: irhee
# section: 1G0
#################################################

import cs112_f20_week8_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

# from: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

#################################################
# Functions for you to write
#################################################

def friendsOfFriends(friends):
    '''
    takes a dict of people and their respective set of friends
    returns a dictionary of the same people mapping to sets
    of friends of friends
    '''
    friendsOfFriends = dict()
    #loops thru each person 
    for currPerson in friends: 
        friendsOfFriends[currPerson] = set()
        #loops through of all current person friends
        for myFriend in friends[currPerson]:  
            #loops through friends of current person friends
            for friendsFriend in friends[myFriend]:
                #if they are not friends w current person and not current person
                if friendsFriend not in friends[currPerson] \
                    and friendsFriend != currPerson:
                    friendsOfFriends[currPerson].add(friendsFriend)

    return friendsOfFriends

#################################################
# Test Functions
#################################################

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    d = dict()
    d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
    d["wilma"] = set(["fred", "betty", "dino"])
    d["betty"] = d["barney"] = d["bam-bam"] = d["dino"] = set()
    fof = friendsOfFriends(d)
    assert(fof["fred"] == set(["dino"]))
    assert(fof["wilma"] == set(["barney", "bam-bam"]))
    result = { "fred":set(["dino"]),
               "wilma":set(["barney", "bam-bam"]),
               "betty":set(),
               "barney":set(),
               "dino":set(),
               "bam-bam":set()
             }
    assert(fof == result)
    d = dict()
    #                A    B    C    D     E     F
    d["A"]  = set([      "B",      "D",        "F" ])
    d["B"]  = set([ "A",      "C", "D",  "E",      ])
    d["C"]  = set([                                ])
    d["D"]  = set([      "B",            "E",  "F" ])
    d["E"]  = set([           "C", "D"             ])
    d["F"]  = set([                "D"             ])
    fof = friendsOfFriends(d)
    assert(fof["A"] == set(["C", "E"]))
    assert(fof["B"] == set(["F"]))
    assert(fof["C"] == set([]))
    assert(fof["D"] == set(["A", "C"]))
    assert(fof["E"] == set(["B", "F"]))
    assert(fof["F"] == set(["B", "E"]))
    result = { "A":set(["C", "E"]),
               "B":set(["F"]),
               "C":set([]),
               "D":set(["A", "C"]),
               "E":set(["B", "F"]),
               "F":set(["B", "E"])
              }
    assert(fof == result)

    #----------------from hw writeup-----------------------
    d = { }
    d["jon"] = set(["arya", "tyrion"])
    d["tyrion"] = set(["jon", "jaime", "pod"])
    d["arya"] = set(["jon"])
    d["jaime"] = set(["tyrion", "brienne"])
    d["brienne"] = set(["jaime", "pod"])
    d["pod"] = set(["tyrion", "brienne", "jaime"])
    d["ramsay"] = set()
    fof = friendsOfFriends(d)
    result = { 'tyrion': {'arya', 'brienne'}, 
                'pod': {'jon'}, 
                'brienne': {'tyrion'}, 
                'arya': {'tyrion'}, 
                'jon': {'pod', 'jaime'}, 
                'jaime': {'pod', 'jon'}, 
                'ramsay': set()
                }
    assert(fof == result)
    print("Passed!")



#################################################
# testAll and main
#################################################

def testAll():
    testFriendsOfFriends()

def main():
    cs112_f20_week8_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
