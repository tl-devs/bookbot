from stats import book_text_word_cnt, book_text_char_cnt

def main():
    test_file_path = "books/frankenstein.txt"
    book_len = book_text_word_cnt(test_file_path)
    print(f"Found {book_len} total words")

    for key, value in book_text_char_cnt(test_file_path).items():
        print(f"'{key}': {value}")

main()