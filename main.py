import sys
from stats import count_words, count_chars, dict_to_list, sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def sort_on(items):
    return items["num"]

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    booktext = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print("Found " + str(count_words(booktext)) + " total words")
    print("--------- Character Count -------")
    charlist = dict_to_list(count_chars(booktext))
    charlist.sort(reverse=True, key=sort_on)
    for item in charlist:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()