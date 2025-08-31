def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
    return file_contents

def get_num_words():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = book_text.split()
    word_count = len(num_words)
    #for word in num_words:
    #    word_count += 1
    print (f"{word_count} words found in the document")




def get_char_count():
    book_text = get_book_text("./books/frankenstein.txt").lower()
    char_count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "0": 0,
        ",": 0,
        ".": 0,
        "!": 0,
        "?": 0,
        "'": 0,
        " ": 0,
        ";": 0,
        ":": 0,
    }
    for char in book_text:
        if char in char_count:
            char_count[char] += 1
    return(char_count)


get_char_count()