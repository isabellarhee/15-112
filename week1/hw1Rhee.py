#################################################
# hw1.py
#
# Your name: Isabella Rhee
# Your andrew id: irhee
#################################################

import cs112_f20_week1_linter
import math

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

#################################################
# hw1-standard functions (for you to write)
#################################################

def eggCartons(eggs):
    if (eggs % 12 == 0):
        return eggs // 12
    else:
        return (eggs // 12) + 1

def nearestBusStop(street):
    HowFar = street % 8
    if (HowFar <= 4):
        return (street // 8) * 8
    else:
        return (street // 8) * 8 + 8

def getKthDigit(n, k):
    if (n < 0):
        n *= -1
    temp1 = n // (pow(10,k))
    return temp1 % 10

def setKthDigit(n, k, d):
    if (n < 0):
        neg = True
        n = abs(n)
    else:
        neg = False

    temp1 = n - (n % (pow(10,k+1)))
    temp2 = d * (pow(10,k))
    if (k > 0):
        temp3 = n % (pow(10,k))
    else:
        temp3 = 0

    if (neg):
        return -1 * (temp1 + temp2 + temp3)
    else:
        return temp1+temp2+temp3
    

def numberOfPoolBalls(rows):
    return (rows * (rows + 1)) / 2

def numberOfPoolBallRows(balls):
    #triRoot = (pow((8 * balls) + 1,(1/2)) - 1) // 2
    temp = pow((8*balls + 1),(1/2))
    
    if temp % 1 == 0 :
        return ((pow((8 * balls) + 1,(1/2))) - 1) // 2
    else:
        temp = ((pow((8 * balls) + 1,(1/2))) - 1) // 2
        temp = (temp // 1)
        return temp + 1



#################################################
# hw1-spicy functions (for you to write)
#################################################
        
def playThreeDiceYahtzee(dice):
    return 42

def handToDice(hand):
    dice1 = getKthDigit(hand, 2)
    dice2 = getKthDigit(hand, 1)
    dice3 = getKthDigit(hand, 0)

    return (dice1, dice2, dice3)

def diceToOrderedHand(a, b, c):
    high = (max(a, b, c)) * 100
    low = min(a,b,c)
    if ((a != high) & a != low):
        mid = a * 10
    elif ((b != high) & (b != low)):
        mid = b * 10
    else:
        mid = c * 10

    return high + mid + low 

def playStep2(hand, dice):
    dice1, dice2, dice3 = handToDice
    

#################################################
# hw1-bonus functions (for you to write)
#################################################

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    point1 = intersect(m1, b1, m2, b2)
    point2 = intersect(m2,b2,m3,b3)
    point3 = intersect(m3,b3,m1,b1)

    side1 = distance(point1, point2)
    side2 = distance(point2, point1)
    side3 = distance(point3, point1)

    return triArea(side1, side2, side3)

def intersect(m1,b1,m2,b2):
##need to figure out
    return x, y

def distance(point1, point2):
   # x1 = point1[0]
   # x2 = point2[0]
   # y1 = point1[1]
   # y1 = point2[1]
    temp1 = pow((x2 - x1), 2)
    temp2 = pow((y2 - y1), 2)
    return pow((temp1 + temp2), (1/2))

def triArea(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    area = pow((s * (s - s1) *(s - s2) * (s - s3)), (1/2))
    return area

def colorBlender(rgb1, rgb2, midpoints, n):
    return 42

def findIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Test Functions
#################################################

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed.')

def testNearestBusStop():
    print('Testing nearestBusStop()... ', end='')
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed.')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed.')

def testPlayThreeDiceYahtzee():
    print('Testing playThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(playThreeDiceYahtzee(2312413) == (432, 4))
    assert(playThreeDiceYahtzee(2315413) == (532, 5))
    assert(playThreeDiceYahtzee(2345413) == (443, 18))
    assert(playThreeDiceYahtzee(2633413) == (633, 16))
    assert(playThreeDiceYahtzee(2333413) == (333, 29))
    assert(playThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def testThreeLinesArea():
    print('Testing threeLinesArea()... ', end='')
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 25), 272.25))
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = findIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # hw1-standard
    testEggCartons()
    testNearestBusStop()
    testGetKthDigit()
    testSetKthDigit()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()

    # hw1-spicy
   # testPlayThreeDiceYahtzee()

    # hw1-bonus
   # testThreeLinesArea()
   # testColorBlender()
   # testFindIntRootsOfCubic()

def main():
    cs112_f20_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
