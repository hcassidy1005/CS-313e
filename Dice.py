#  File: Dice.py
#  Description: Makes a histogram of the result of rolling two dice multiple times
#  Student's Name: Hailey Cassidy
#  Student's UT EID: HAC787
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 9/11/17
#  Date Last Modified: 9/13/17

import random

def main():
    random.seed(1314)
    
    #input the number of rolls
    numRolls = eval(input("How many times would you like to roll the dice? "))
    
    #define variables 
    numTwos = 0
    numThrees = 0
    numFours = 0
    numFives = 0
    numSixes = 0
    numSevens = 0
    numEights = 0
    numNines = 0
    numTens = 0
    numElevens = 0
    numTwelves = 0

    #rolling the dice 
    i = 1
    while (i <= numRolls):
        roll = random.randint(1,6) + random.randint(1,6)
        if (roll == 2):
            numTwos += 1
        elif (roll == 3):
            numThrees += 1
        elif (roll == 4):
            numFours += 1
        elif (roll == 5):
            numFives += 1
        elif (roll == 6):
            numSixes +=  1
        elif (roll == 7):
            numSevens += 1
        elif (roll == 8):
            numEights += 1
        elif (roll == 9):
            numNines += 1
        elif (roll == 10):
            numTens += 1
        elif (roll == 11):
            numElevens += 1
        else:
            numTwelves += 1
        i += 1

    #making and displaying the results list
    results = [numTwos, numThrees, numFours, numFives, numSixes, numSevens, numEights, numNines, numTens, numElevens, numTwelves]
    print("Results:",results)
    
    #accounting for a large amount of rolls 
    if (numRolls > 100):
        x = 0
        while (x < 11):
            value = results[x]
            results.remove(results[x])
            results.insert(x, ((value * 100) / numRolls))
            x += 1
        
    #printing histogram
    heightHist = max(results)
    histPrint = ""
    while (heightHist > 0):
        histPrint += " | "
        z = 0
        while (z < 11):
            if (results[z] >= heightHist):
                histPrint += " * "
            else:
                histPrint += "   "
            z = z + 1
        if (heightHist > 1):
            histPrint += "\n"
        heightHist -= 1
        
    print("")
    print(histPrint)
    print(" +__+__+__+__+__+__+__+__+__+__+__+_")
    print("    2  3  4  5  6  7  8  9 10 11 12 ")
    
main()
