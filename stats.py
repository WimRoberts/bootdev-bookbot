def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = 0
    for word in book_text.split():
        num_words += 1
    print(f"{num_words} words found in the document")

def get_char_count():
    book_text = get_book_text("./books/frankenstein.txt").lower()
    num_chars = {}
    for char in book_text:
        if char not in num_chars:
            num_chars[char] = 1
        else:
            num_chars[char] += 1
    return num_chars