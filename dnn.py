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
parser.add_argument("-TLD", "--extension", help="Domain extension/TLD", default=".com", type=str)
parser.add_argument("-RP", "--resultspath", help="Path to save the generated domain list results", default='Results', type=str)
parser.add_argument("-LP", "--listpath", help="Path to wordlists directory", default='Word Lists', type=str)
parser.add_argument("-L1", "--wordlist1", help="Path to wordlist1", default='sampleList1.txt', type=str)
parser.add_argument("-L2", "--wordlist2", help="Path to wordlist2", default='sampleList2.txt', type=str)
args = parser.parse_args()

#paths take in arguments
save_path = args.resultspath
wL_path = args.listpath

#change file name prefix
newList = "newList"

#TLD/Extension take in arguments
TLDs = args.extension.split(", ")

#change file suffix & output
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
filename = "_".join([newList, suffix]) # e.g. 'mylogfile_120508_171442'

#change file extension
completeName = os.path.join(save_path, filename+".txt")

#Enter file locations here to change combo lists
WordList1 = os.path.join(wL_path, args.wordlist1)
WordList2 = os.path.join(wL_path, args.wordlist2)

#while loop
count = 0
add = count + 1


#SectionA
#writes file to directory specified above after loop
with open(completeName, 'w') as f:
    def combineLists():
        result_list = []  # Create an empty list to store the results
        count = 0
        while (count < 500):
            count = count + 1
            resultTLD = (random.choice(TLDs))
            resultA = (random.choice(open(WordList1).read().split()).strip())
            resultB = (random.choice(open(WordList2).read().split()).strip())
            randomOrder = random.choice("AB")
            if (randomOrder == "A"):
                domain = resultA + resultB + resultTLD
            else:
                domain = resultB + resultA + resultTLD
            result_list.append(domain)  # Append the domain to the result list
            f.write(domain)  # Write the domain to the file
            if (count < 500):
                f.write('\n')
        return result_list  # Return the result list
    
    # Execute the function and store the result list in a variable
    result_list = combineLists()

with open(completeName, 'r') as f:
    # Copy contents of text file to clipboard
    pyperclip.copy(f.read())
    
    #print success
    print("WordList1 and WordList2 have been combined and copied to your clipboard with your preferred TLD(s): " + ', '.join(TLDs))

with open(completeName, 'w') as f:
    # Section B Write lines to the text file
    f.write("WordList1 and WordList2 have been combined and copied to your clipboard with your preferred TLD(s): " + ', '.join(TLDs) + '\n\n')
    f.write("WordList1: " + WordList1 + "\nWordList2: " + WordList2 + "\n\n")
    f.write("Check their availability at https://www.name.com/names using the bulk search utility, sort by price, and go! \n")
    f.write("Be sure to check out DavidInfosec.com for more awesome tools! " + '\n\n')
    f.write("Your generated domains:\n")
    # End of Section B
    f.write('\n'.join(result_list))


    

    
subprocess.Popen(completeName, shell=True)


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
