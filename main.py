from stats import book_text_word_cnt

def main():
    test_file_path = "books/frankenstein.txt"
    book_len = book_text_word_cnt(test_file_path)
    print(f"Found {book_len} total words")

main()