# Domain-Name-Ninja

Domain Name Ninja, a nimble and agile tool, swiftly slices through word lists like a masterful ninja. With precision and artistry, it forges unique and powerful domain names. Unleash the stealth and finesse of Domain Name Ninja to conquer the domain registration battlefield with ease. 

## Getting Started
1. If you haven't already installed Python, please download and install it from the official Python website (https://www.python.org) based on your operating system.
2. Clone the repository or download the .zip file from the GitHub repository containing the Domain Name Ninja application.
3. Extract the contents of the downloaded .zip file to a location of your choice on your computer.
4. Open the extracted folder named "Domain-Name-Ninja-main."
5. Take note of the file path of the extracted folder. For example, on Windows, the file path might look like "C:\Users<username><somelocation>\Domain-Name-Ninja-main"
6. Open a terminal or command prompt instance on your computer.
7. Change your current directory to the location of the extracted folder using the "cd" command.
  For instance, if the file path is "C:\Users<username><somelocation>\Domain-Name-Ninja-main", you would enter the following command:
  ``cd C:\Users\<username>\<somelocation>\Domain-Name-Ninja-main\``
  
8. Once you are in the correct directory, run the following command to install dependencies:

   ``pip install pyperclip``

9. Now, simply execute the program by executing the command:
  ``python dnn.py --help``

By following these instructions, you should be able to run the Domain Name Ninja application successfully.

  
## Usage

The script dnn.py can be run from the command line by calling python dnn.py with the following optional arguments:
-   `-TLD` or `--extension` : Domain extension/TLD (default is '.com')
-   `-RP` or `--resultspath` : Path to save the generated domain list (default is 'Results')
-   `-LP` or `--listpath` : Path to wordlists directory (default is 'Word Lists')
-   `-L1` or `--wordlist1` : Path to wordlist 1 (default is 'sampleList1.txt')
-   `-L2` or `--wordlist2` : Path to wordlist 2 (default is 'sampleList2.txt')
-   `-OA` or `--outputamount` : Number of domains to output (default is 100, type=int)
-   `-TS` or `--textsummary` : Pops up a text file recap of the generated domains (default is False)
-   `-FN` or `--filename` : Custom file name prefix (default is newList)
-   `-h` or `--help`: Refer to the help menu

## Example

`python dnn.py -TLD '.com' -RP 'my_results' -LP 'my_wordlists' -L1 'list1.txt' -L2 'list2.txt' -TS -FN 'awesomedomains'
`

This command will run the script with the TLD '.com', save the generated domain list to the 'my_results' directory, use the wordlists located in the 'my_wordlists' directory, and combine the lists 'list1.txt' and 'list2.txt'. It will also show a text summary of the generated domains and save the generated domain list to a text file named 'awesomedomains_<current date and time>.txt' in the specified results path directory, and copy it to the clipboard.

To view the help menu, run the script with the -h or --help option.

example : `python dnn.py --help`


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

