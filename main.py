from stats import get_num_words
from stats import get_char_count
from stats import sort_char_count


char_count = get_char_count()
sorted_char_count = sort_char_count(char_count)
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words()
    print("-------- Character Count --------")
    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")

main()
