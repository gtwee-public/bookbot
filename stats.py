def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def split_words(str):
    words = str.split()
    count = len(words)
    return count

def get_num_words():
    print(f" Found {split_words(get_book_text())} total words")

def count_each_character():
    book_text = get_book_text().lower()
    text_count = {}

    for text in book_text:
        if text in text_count:
            text_count[text] += 1
        else:
            text_count[text] = 1

    print(text_count)

