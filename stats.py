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
