def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()

    return file_content

def book_text_word_cnt(input_book):
    split_book = input_book.split()
    return len(split_book)