def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = 0
    for word in book_text.split():
        num_words += 1
    print(f"Found {num_words} total words")

def get_char_count():
    book_text = get_book_text("./books/frankenstein.txt").lower()
    num_chars = {}
    for char in book_text:
        if char not in num_chars:
            num_chars[char] = 1
        else:
            num_chars[char] += 1
    return num_chars

def sort_on(items):
    return items["num"]

def sort_char_count(char_count):
    blank_char_count = []
    for key in char_count:
        #sorted_char_count[key] = char_count[key]
        temp_dict = {}
        if key.isalpha():
            temp_dict["char"] = key
            temp_dict["num"] = char_count[key]
            blank_char_count.append(temp_dict)
    blank_char_count.sort(key=sort_on, reverse=True)
    return blank_char_count

