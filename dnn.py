import argparse
import datetime
import random
import subprocess
import os.path
import pyperclip
import sys
import time
random.seed(time.time())

parser = argparse.ArgumentParser()
parser.add_argument("-TLD", "--TLD", help="Domain extension/TLD", default=".com", type=str)
parser.add_argument("-sP", "--savePath", help="Path to save the generated domain list", default='Results', type=str)
parser.add_argument("-wlP", "--wordListPath", help="Path to wordlists directory", default='wLists', type=str)
parser.add_argument("-L1", "--wordList1", help="Path to wordlist 1", default='sampleList1.txt', type=str)
parser.add_argument("-L2", "--wordList2", help="Path to wordlist 2", default='sampleList2.txt', type=str)
args = parser.parse_args()

#paths take in arguments
save_path = args.savePath
wL_path = args.wordListPath

#change file name prefix
newList = "newList"

#TLD/Extension take in arguments
TLDs = args.TLD.split(", ")

#change file suffix & output
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
filename = "_".join([newList, suffix]) # e.g. 'mylogfile_120508_171442'

#change file extension
completeName = os.path.join(save_path, filename+".txt")

#Enter file locations here to change combo lists
WordList1 = os.path.join(wL_path, args.wordList1)
WordList2 = os.path.join(wL_path, args.wordList2)

#while loop
count = 0
add = count + 1

#writes file to directory specified above after loop
with open(completeName, 'w') as f:
    def combineLists():
        count = 0
        while (count < 500):
            count = count + 1
            resultTLD = (random.choice(TLDs))
            resultA = (random.choice(open(WordList1).read().split()).strip())
            resultB = (random.choice(open(WordList2).read().split()).strip())
            randomOrder = random.choice("AB")
            if (count > 1):
                f.write('\n')
            if (randomOrder == "A"):
                f.write(resultA + resultB + resultTLD)
            else:
                f.write(resultB + resultA + resultTLD)


    #prints and writes a console/file completion message
    print("WordList1 and WordList2 have been combined with your preferred TLD(s): " + ', '.join(TLDs))

    #executes function
    combineLists()

# Open the file for writing in the beginning
with open(completeName, 'w') as f:
    f.write("WordList1 and WordList2 have been combined and copied to your clipboard with your preferred TLD(s): " + ', '.join(TLDs) + '\n\n')
    f.write("WordList1: " + WordList1 + "\nWordList2: " + WordList2 + "\n\n")
    f.write("Check their availability at https://www.name.com/names using the bulk search utility, sort by price, and go! \n")
    f.write("Be sure to check out DavidInfosec.com for more awesome tools! " + '\n\n')
    f.write("Your generated domains:\n")
    combineLists()
    subprocess.Popen(completeName, shell=True)
    
    # clipboard.copy(fo)
pyperclip.copy(open(completeName, 'r').read())

def help():
    print("Usage: python dnn.py [options]\n")
    print("Options:")
    print("-TLD, --TLD\t\tDomain extension/TLD (default: '.com, .org, .co')")
    print("-sP, --savePath\t\tPath to save the generated domain list (default: 'Results')")
    print("-wlP, --wordListPath\tPath to wordlists directory (default: 'wLists')")
    print("-L1, --wordList1\t\tPath to wordlist 1 (default: 'sampleList1.txt')")
    print("-L2, --wordList2\t\tPath to wordlist 2 (default: 'sampleList2.txt')")
    print("-h, --help\t\tShow this help menu\n")
    print("Example: python dnn.py -TLD .com -sP my_results -wlP my_wordlists -L1 list1.txt -L2 list2.txt")

def main():
    if __name__ == "__main__":
        if "-h" in sys.argv or "--help" in sys.argv:
            help()
        else:
            main()
