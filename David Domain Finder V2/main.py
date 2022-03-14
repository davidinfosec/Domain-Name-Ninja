import datetime
import random
import subprocess
import os.path
import clipboard
import sys

#change domain extension
extension = (".com",)


#change save paths
save_path = 'C:/Users/<user>/PycharmProjects/David Domain Finder V2/exportedLists'
ComboPath = 'C:/Users/<user>/PycharmProjects/David Domain Finder V2/Word Combos'

#change file name prefix
newList = "newList"

#change file suffix & output
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
filename = "_".join([newList, suffix]) # e.g. 'mylogfile_120508_171442'

#change file extension
completeName = os.path.join(save_path, filename+".txt")

#Enter file locations here to change combo lists

#A
ComboFileA = 'C:/Users/<user>/PycharmProjects/David Domain Finder V2/Word Combos/4L.txt'

#B
ComboFileB = 'C:/Users/<user>/PycharmProjects/David Domain Finder V2/Word Combos/5 letter words.txt'

#while loop
count = 0
add = count + 1

#writes file to directory specified above after loop
with open(completeName, 'w') as f:

# While loop - generates 100 potential domains by contactenating the two lists randomly, adds a desired extension,
# and then exports to a text file in exportedLists directory. (Can be changed by changing to 100 to any integer.
    def combineLists():
     count = 0
    while (count < 500):
        count = count + 1

        #Comment B out if you only want to use one list. (make sure to remove from print statement also, but don't forget
        #to put it back!

        resultA = (random.choice(open(ComboFileA).read().split()).strip())
        resultB = (random.choice(open(ComboFileB).read().split()).strip())

#swaps prefix/suffix of lists randomly
        randomOrder = random.choice("A" + "B")
        if (randomOrder == "A"):
            print(resultA + resultB + random.choice(extension), file=f)
        else:
            print(resultB + resultA + random.choice(extension), file=f)

#prints a console completion message
print("List A & B have been combined.")

fo = open(completeName, 'r').read()
clipboard.copy(fo)

#executes function
combineLists()

























