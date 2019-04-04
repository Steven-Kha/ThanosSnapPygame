'''

This program mimicks resetera's thanos snap
i read a list of names for names.txt line by line and added it to a list
now i shall randomize the list for fairness
the top two names of the list will face each other.
One shall be The Chosen.
The other, the Avenger


data structures to use:
a list to read all the names in the text file
a stack with two names that face each other
  - One shall be Chosen, the other shall be the Avenger

libraries:
random library helps you just use shuffle lol

steps to the program:
1. load all the biotic
2. randomize the names
3. If len(biotic) > 1
    a: go to step 4
   else:
    a: go to step 5
4. Get the two st
5.


'''

import time

import random

def load():
    # read each name line by line and append it to biotic vector
    biotic = []
    read_file = open("names.txt", "r")
    loadVector = read_file.read().splitlines()
    vectorSize = len(loadVector)
    if vectorSize < 0:
        return None
    for i in range(vectorSize):
        biotic.append(loadVector[i])
    return biotic

def versus(fiftyFifty, biotic, chosen, avenger, lastOne, lastOneChosen):
    # error handling for biotic size
    # maybe a function would be better
    # also how two names fight each other
    # BUT WHAT HAPPENS WHEN ONLY ONE NAME IS LEFT?

    #coin toss. Choose a number between 0 and 1.
    # if it matches the index, you are Chosen

    #initialize first in case
    call = 0

    #randomly set it to 0 or 1
    call = random.randint(0, 1)

    if len(biotic) > 1:
        fiftyFifty.append(biotic.pop())
        fiftyFifty.append(biotic.pop())
    elif len(biotic) > 0:
        lastOne = True
        oddNameLeft(biotic, lastOneChosen, chosen, avenger)
        return False
    else:
        return False

    #pop the stack too
    chosen.append(fiftyFifty[call])
    del fiftyFifty[call]
    avenger.append(fiftyFifty.pop())
    return True

def oddNameLeft(biotic, lastOneChosen, chosen, avenger):

    #call 0 or 1 where 0 is tails and 1 is heads
    call = 0

    #the result of the coin toss
    result = 0

    call = random.randint(0, 1)
    result = random.randint(0, 1)

    if call == result:
        chosen.append(biotic.pop())
        lastOneChosen = True
        #print("Last one chosen is True!")
        print(str(chosen[len(chosen) - 1]) + " has fallen.")

    else:
        avenger.append(biotic.pop())
        #print("Last one chosen is False!")
        print(str(avenger[len(avenger) - 1]) + " is an avenger.")


    return True


def writeMatchUp(chosen, avenger):
    #first two lines lets you reset the text files over without going out of indices bound
    writeFile = open("matchup.txt", "w")
    writeFile.close()

    writeFile = open("matchup.txt", "w")
    if range(len(chosen) > len(avenger)):
        for i in range(len(avenger)):
            writeFile.write(str(chosen[i]) + " vs. " + str(avenger[i]) + "\n")

    if range(len(avenger) > len(chosen)):
        for i in range(len(chosen)):
            writeFile.write(str(chosen[i]) + " vs. " + str(avenger[i]) + "\n")

    if range(len(chosen) > len(avenger)):
        writeFile.write(str(chosen[len(chosen)-1]) + " vs. " + "fate \n")
    if range(len(avenger) > len(chosen)):
        writeFile.write(str(avenger[len(avenger)-1]) + " vs. " + "fate \n")

    writeFile.close()

def writeChosen(chosen):
    writeFile = open("chosen.txt", "w")
    writeFile.close()

    writeFile = open("chosen.txt", "w")
    for i in range(len(chosen)):
        writeFile.write(str(chosen[i]) + "\n")
    writeFile.close()

def writeAvenger(avenger):
    writeFile = open("avenger.txt", "w")
    writeFile.close()

    writeFile = open("avenger.txt", "w")
    for i in range(len(avenger)):
        writeFile.write(str(avenger[i] + "\n"))
    writeFile.close()







