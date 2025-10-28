file_location = "books/frankenstein.txt"

def get_book_text():
    with open(file_location) as f:
        file_contents = f.read()
        return file_contents

def split_words(str):
    words = str.split()
    count = len(words)
    return count

def get_num_words():
    print(f" Found {split_words(get_book_text())} total words")

def sort_characters(characters):
    return characters["data"]

def count_each_character():
    book_text = get_book_text().lower()
    text_count = {}
    
    for text in book_text:
        if text in text_count:
            text_count[text] += 1
        else:
            text_count[text] = 1
    return text_count

def split_and_sort():
    dictionary = count_each_character()

    # Convert each key-value pair into a separate dictionary
    individual_dicts = {k: v for k, v in dictionary.items() if k != ' '}

    # Sort the dictionary by value (descending)
    sorted_list = sorted(individual_dicts.items(), key=lambda x: x[1], reverse=True)

    # Print them line by line
    for item in sorted_list:
        print(f"{item[0]}: {item[1]}")


