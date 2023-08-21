# Harvard CS50p final project: COUNTRIES


## Video Demo:  <https://youtu.be/Dni5MiR7Or0>


#### To use the program, the following is required: 
1. 'countries.py' file  
2. 'file_functions' folder containing:
    - 'file_functions/analysis.py'
    - 'file_functions/countries_writer.py'
3. pip install all modules outlined in requirements.txt:
    - os
    - re
    - art
    - sys
    - requests
    - csv
    - matplotlib

## Contents:
#### 1. Main file, 'countries.py' containing 9 functions: 
    1.1. read_countries (contains write_countries from 'countries_writer.py' , see 2.1)  
    1.2. check_countries  
    1.3. near_match   
    1.4. misspell_match   
    1.5. abbreviate_match   
    1.6. recommend options  
    1.7. get_data  
    1.8. round_sig_figs  
    1.9. confirm_selection  
    1.10 analysis_countries (located within 'analysis.py' , see 2.2)  
#### 2. File of functions (file_functions) used by main file:  
    2.1. 'countries_writer.py'  
    2.2. 'analysis.py'  



## 1. Main file: 'countries.py'
Prompts users for countries of the world. The user can then compare different metrics for each country in a list or through graphical visualisation. At the end of the program, user data (graphs and sorted list) is saved in a folder called user_data.

If the user inputs ctr + c at any time, the terminal window is cleared and a message is displayed, thanking the user for trying the program.

### 1.1. read_countries()
If the user directory does not have the file containing the sorted list of countries, the write_countries function is called from "countries_writer.py" (see section 2.1). Once the file of 245 countries in alphabetical order is available in the local directory, read_countries reads the contents line by line of the sorted country file and returns the result as a list to the main function.

### 1.2. check_countries(list)
The user is promted for a country which is checked against the list of countries passed to the function. If the user does not input valid format, they are reprometed. Valid formatting contains no punctuation or numbers, the user may only enter characters and spaces. After receiving a valid entry, one by one  the input is run through the three spell checking algorithms: near_match (1.3), misspell match (1.4), and abbreviate match (1.5). If any return 'True', the input is a valid country within the list and the user is asked to confirm their selection with a 'y' or 'n'. If the user inputs 'n', they enter another string, if yes, the check_countries function returns their selected country.

### 1.3. near_match(input, list)
Takes a value (input) and a list. Iterates over the list and searches for exact or near matches (case insensitive) with the input.
Matches are made when containing all the same letters except one missing letter at the start or the end of the word.
E.g., "egyp" or "gypt" will return Egypt and "egyptr" will also return egypt
The user may also type a string and as long as an item within the list is inside the value string it will produce a match.
E.g., "my country is japan" will return Japan

### 1.4. mispell_match(input, list)
Takes a value (input) and list. Iterates over the list and searches for a match (case insensitive) with the input valie if it is mispelled.
Matches if the mispelled word:
    -is within 20% similarity in length to the item
    -starts with the same letter as the item
    -contains the same letters to the item (with room for 20% spelling error by number of incorrect letters)
        --words with 5-9 letters accept 1 letter misspelled
        --words with 10-14 letters accept 2 letters mispelled
        --etc
E.g., spain (5 letters) will match with (1 wrong character): sapin, span, spian, spaun, stain.
E.g., united states (12 letters) will match with (2 wrong characters): uited sates, united stes, unted state.

### 1.5. abbreviate_match(input, list)
Takes a value (input) and list. Iterates over the list and searches for a match (case insensitive) with the input value if it is an abbreviation of any item in the list.
E.g., US will match united states, uae will match united arab emirates.

The word and is excluded from the abbreviation:
E.g., HIMI matches: Heard Island and McDonald Islands (HIAMI will not match).

### 1.6. recommend_options(input, list)
If, within check_countries (see 1.2), the input value does not match with any of the spell check algorithms, the user is provided with a list of all the countries within the list that start with the same letter as their input. The user can then enter (by typing or copying and pasting) an item from the recommended list. The check_countries algorithm repeats with the new input, checking the ENTIRE sorted countries list (variable called 'countries').

### 1.7. get_data(user_country_name)
Once the user has confirmed their selected country, a request (requests library) is sent to:
https://api.api-ninjas.com/v1/country?name= + {user_country_name}.
This returns values specific to the country which are filtered into a dictionary of GDP, Population, Life Expectancy and CO2
emissions for the user selected country. If no data is available for any field it is given the value "N/A". The function returns
the dictionary and it is appended to a list of user country data in main. 1.2 - 1.7 is repeated until the user decides they have
selected all the countries they would like, or their list of countries reaches the maximum value (currently set as 10, a global value
which may only be changed with access to the code. i.e., at top of function change max=10, to max = n)

### 1.8. round_sig_figs(n , figs)
Used by get_data, this function rounds a number (n) to a specified number of significant figures (figs).

### 1.9. confirm_selection(countries_data , countries)
The user is shown the list of countries they have selected in the program (countries_data), the user can then change a country for another, or add a country if size of the list is below the maximum value. If the user tries to enter a country already in the list, the list remains unchanged.

### 1.10 analysis_countries(countries_data)
Main uses this function, from file_functions/analysis.py. The analysis.py file is run with the users selected countries (list of dictionaries called countries_data). See 2.2 for function description.


## 2. Functions file: 'file_functions'

### 2.1. countries_writer.py
The write countries function is this file checks if the user already has the file of sorted countries
(sorted_countries.txt), if not, the function checks if the user has a file of unsorted countries (countries_raw.csv). If there is no file of unsorted countries, the function pulls 246 countries from a request to a github repository of country info (https://github.com/google/dspl/blob/master/samples/google/canonical/countries.csv).
It then creates a local file ("sorted_countries") and writes a list of 246 countries in alphabetical order.
If the github link becomes null, there is a backup file for writing the sorted countries list using a local file in: backup_writer called "backup_countries_writer".

### 2.2. analysis_countries
If the user does not have a local file of user data (called 'user_data), it is created. In this file, sorted lists and graphs are stored as the user runs the program.

Takes the list of countries provided in section 1 and allows user to sort list by different metrics, and view graphical visualisations of the sorted data. Metrics include Country name GDP, Population, Life Expectancy and CO2 emissions. No visualisation is available for countries sorted by name in alphabeitcal order, but for all other fields the user is provided the option to view the result as a graph. After being viewed, graphs are automatically saved to the user_data folder.
At the end of the program the user is asked if they wish to save their sorted list. If 'y' or 'yes' (case insensitive), the sorted list is saved to the user_data as a csv file, with a note at the bottom describing which field the data is sorted by (e.g., #SORTED BY Population)

