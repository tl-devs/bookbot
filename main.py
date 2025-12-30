from stats import *

def main():
    test_file_path = "books/frankenstein.txt"
    book = get_book_text(test_file_path)
    book_len = book_text_word_cnt(book)
    print(f"Found {book_len} total words")

main()