# Domain-Name-Ninja
Domain Finder

This is David's Domain Finder with a fresh coat of paint. Now accepting arguments and ultimately streamlining the process. Read through the pictures to understand how it works, and streamline your domain hand-registrations. Let Domain Name Ninja do the heavy lifting.

## Usage

The script dnn.py can be run from the command line by calling python dnn.py with the following optional arguments:
- -TLD or --extension : Domain extension/TLD (default is '.com')
- -RP or --resultspath : Path to save the generated domain list (default is 'Results')
- -LP or --listpath : Path to wordlists directory (default is 'Word Lists')
- -L1 or --wordlist1 : Path to wordlist 1 (default is 'sampleList1.txt')
- -L2 or --wordlist2 : Path to wordlist 2 (default is 'sampleList2.txt')
- -OA or --outputamount: Number of domains to output (default is 100, type=int)
- -TS or --textsummary : Pops up a text file recap of the generated domains (default is False)
- -FN or --filename : Custom file name prefix (default is newList)
- -h or --help: Refer to the help menu

## Example

`python dnn.py -TLD '.com' -RP 'my_results' -LP 'my_wordlists' -L1 'list1.txt' -L2 'list2.txt' -TS -FN 'awesomedomains'
`
This command will run the script with the TLD '.com', save the generated domain list to the 'my_results' directory, use the wordlists located in the 'my_wordlists' directory, and combine the lists 'list1.txt' and 'list2.txt'. It will also show a text summary of the generated domains and save the generated domain list to a text file named 'awesomedomains_<current date and time>.txt' in the specified results path directory, and copy it to the clipboard.

To view the help menu, run the script with the -h or --help option.

example : python dnn.py --help


## Note

Be sure to check the availability of the generated domain names at [https://www.name.com/names](https://www.name.com/names) using the bulk search utility, sort by price, and go! Also, check out https://www.DavidInfosec.com or follow me on GitHub for more awesome tools!


## Images - dnn.py
Run it default with the stored sample lists:
![Domian Name Ninja command line](https://i.imgur.com/SdRwTla.png)

File opens with important information:
![Domain Name Ninja text summary](https://i.imgur.com/UIaBp83.png)

Enjoy bulk searching for your new domain names:
![bulk search on Name.com](https://i.imgur.com/cWZLqj7.png)

### Images - run.bat
![Domain Name Ninja batch file](https://i.imgur.com/vA9Hpy2.png)
![Domain Name Ninja batch file run](https://i.imgur.com/rTeSgS5.png)

