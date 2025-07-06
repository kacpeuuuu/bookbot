from stats import get_num_words
from stats import count_characters
import sys



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------"""
          )
    get_num_words(sys.argv[1])
    print("--------- Character Count -------")
    list_dict = count_characters(sys.argv[1])
    for i in list_dict:
        print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")




main()