# Bookbot main.py

# This file will take in functions and stats from other files 
# to compile the data into a nicely organized manner.

# The main function body of program
def main():
    from stats import get_num_words
    from stats import split_and_sort
    from stats import file_location

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}...")
    print("----------- Word Count ----------")
    
    # Function will take in predetermined file location and return
    # the total number of words in the file.
    get_num_words()
    
    print("--------- Character Count -------")

    # Function will count and sort each individual character from 
    # the file and print the info into the terminal.
    split_and_sort()

    print("============= END ===============")


main()


