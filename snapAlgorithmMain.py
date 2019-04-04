import random
import time
import os
clear = lambda : os.system('cls')
from childrenOfThanos import load, versus, writeChosen, writeAvenger, writeMatchUp

#---------Main --------------------

clear()
#leftRight to alternate who appears left or right in versus lol
leftRight = 0

#name for chosen or avenger
fiftyFifty = []

#list of all living names
biotic = load()

#list of the chosen and the avengers
chosen = []
avenger = []

lastOne = False
lastOneChosen = False

#shuffle the names 100 times
for i in range(100):
    random.shuffle(biotic)

# for i in range(len(biotic)):
#     print(str(i) + ": " + str(biotic[i]))

print("Number of living names at the start: " + str(len(biotic)))

# for i in range(len(fiftyFifty)):
#     print(str(i) + ": " + str(fiftyFifty[i]))

while len(biotic) > 0:

    if len(biotic) > 1:
        print(str(biotic[len(biotic)-1]) + " vs. " + str(biotic[len(biotic)-2]) )
        print("")
    if len(biotic) > 0 and len(biotic) < 2:
        print("Last but not least. " + str(biotic[0]) + "...")
    time.sleep(3)
    #pops the top two biotics or calls oddNameLeft to decide the last name in biotic
    if versus(fiftyFifty, biotic, chosen, avenger, lastOne, lastOneChosen):
        #exit() #has the a print message who is fallen or an avenger
        print(str(chosen[len(chosen)-1]) + " has fallen.")
        print(str(avenger[len(avenger)-1]) + " is an avenger.")
    print("")
    print("Number of names to be decided still: " + str(len(biotic)))
    print("")
    time.sleep(3.5)
    clear()



#write the matchups that occured
writeMatchUp(chosen, avenger)

#sort list alphabetically
chosen.sort(key=str.lower)

avenger.sort(key=str.lower)

#write the names of chosen to textfile
writeChosen(chosen)

#write the names of avengers to textfile
writeAvenger(avenger)