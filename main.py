# Bookbot main.py

# This file will take in functions and stats from other files 
# to compile the data into a nicely organized manner.

import sys
file_location = ""

# The main function body of program
def main():
    # Checks if sys.argv has two entries, stops and explains how
    # to use program if it doesn't.
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        file_location = sys.argv[1]

    from stats import get_num_words
    from stats import split_and_sort

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}...")
    print("----------- Word Count ----------")
    
    # Function will take in file location provided by argument and
    # return the total number of words in the file.
    get_num_words()
    
    print("--------- Character Count -------")

    # Function will count and sort each individual character from 
    # the file and print the info into the terminal.
    split_and_sort()

    print("============= END ===============")


main()


