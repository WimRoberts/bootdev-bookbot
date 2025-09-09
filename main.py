from stats import get_num_words
from stats import get_char_count
from stats import sort_char_count
import sys

#check for proper usage:
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

char_count = get_char_count(sys.argv[1])
sorted_char_count = sort_char_count(char_count)
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_num_words(sys.argv[1])
    print("-------- Character Count --------")
    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")

main()
