from stats import count_words, count_chars, dict_to_list, sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def sort_on(items):
    return items["num"]

def main():
    booktext = get_book_text(r"/mnt/d/Coding/github.com/ptambo/bookbot/books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print("Found " + str(count_words(booktext)) + " total words")
    print("--------- Character Count -------")
    charlist = dict_to_list(count_chars(booktext))
    charlist.sort(reverse=True, key=sort_on)
    for item in charlist:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()