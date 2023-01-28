# Domain-Name-Ninja
Domain Finder

This is David's Domain Finder with a fresh coat of paint. Now accepting arguments and ultimately streamlining the process. Read through the pictures to understand how it works, and streamline your domain hand-registrations. Let Domain Name Ninja do the heavy lifting.

## Overview

This script is a domain name generator that takes in two wordlists, combines them with a random TLD (top-level domain), and generates a new list of domain names. The generated domain names are saved to a file and also copied to the clipboard.

## Usage

The script can be run from the command line by calling `python dnn.py` with the following optional arguments:

-   `-TLD` or `--TLD` : Domain extension/TLD (default is '.com').
-   `-sP` or `--savePath` : Path to save the generated domain list (default is 'Results').
-   `-wlP` or `--wordListPath` : Path to wordlists directory (default is 'wLists').
-   `-L1` or `--wordList1` : Path to wordlist 1 (default is 'sampleList1.txt').
-   `-L2` or `--wordList2` : Path to wordlist 2 (default is 'sampleList2.txt').
-   `-h` or `--help`: Access the help menu.

## Example

`python dnn.py -TLD .com, .net, .org -sP myResults -wlP myWordLists -L1 myList1.txt -L2 myList2.txt`

This command will run the script with the TLDs '.com', '.net', and '.org', save the generated domain list to the 'myResults' directory, use the wordlists located in the 'myWordLists' directory, and combine the lists 'myList1.txt' and 'myList2.txt'.

## Note

Be sure to check the availability of the generated domain names at [https://www.name.com/names](https://www.name.com/names) using the bulk search utility, sort by price, and go! Also, check out DavidInfosec.com for more awesome tools!


## Images
Run it default with the stored sample lists:
![alt text](https://i.imgur.com/SdRwTla.png)

File opens with important information:
![alt text](https://i.imgur.com/UIaBp83.png)

Enjoy bulk searching for your new domain names:
![alt text](https://i.imgur.com/cWZLqj7.png)
