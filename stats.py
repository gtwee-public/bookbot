import sys

# Function will get the contents of the file used for analsys
# and return it as a string
def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents

# Function will take an str as input and split the string into
# words, then it will return the amount of words from that string
def split_words(str):
    count = len(str.split())
    return count

# Function will use the split_words() and get_book_text() functions
# to print the total number of words in the file into a neat sentence
def get_num_words():
    print(f" Found {split_words(get_book_text())} total words")

# Function will take the string of text from get_book_text() function
# and return a count of each individual character as a key pair
# within a dictionary e.g {individual_character: number_of_instances}
def count_each_character():
    book_text = get_book_text().lower()
    text_count = {}
    
    for text in book_text:
        if text in text_count:
            text_count[text] += 1
        else:
            text_count[text] = 1
    return text_count

# Function will take the returned dictionary from count_each_character()
# function and split it into seperate dictionaries per key.
# Then it will sort the dictionaries by value within a list and print
# that sorted list neatly.
def split_and_sort():
    dictionary = count_each_character()

    # Convert each key-value pair into a separate dictionary
    individual_dicts = {k: v for k, v in dictionary.items() if k != ' '}

    # Sort the dictionary by value (descending)
    sorted_list = sorted(individual_dicts.items(), key=lambda x: x[1], reverse=True)

    # Print them line by line
    for item in sorted_list:
        print(f"{item[0]}: {item[1]}")


