import stats as st
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    file_to_process = st.get_book_text(file_path)

    book_len = st.book_text_word_cnt(file_to_process)
    char_cnt = st.book_text_char_cnt(file_to_process)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {book_len} total words")
    print(f"--------- Character Count -------")

    for key, value in char_cnt.items():
        print(f"{key}: {value}")

    print("============= END ===============")

main()