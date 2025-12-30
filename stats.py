def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()

    return file_content

def book_text_word_cnt(input_book):
    book_to_split = get_book_text(input_book)
    split_book = book_to_split.split()
    return len(split_book)