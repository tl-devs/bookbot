from stats import book_text_word_cnt, book_text_char_cnt, sort_on
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_len = book_text_word_cnt(file_path)
    char_cnt = book_text_char_cnt(file_path)#.sort(reverse=True, key=sort_on)

    print(f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {book_len} total words
--------- Character Count -------
""", end="")

    for key, value in char_cnt.items():
        print(f"{key}: {value}")

    print("============= END ===============")

main()