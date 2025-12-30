def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()

    return file_content

def book_text_word_cnt(input_book):
    book_to_split = get_book_text(input_book)
    split_book = book_to_split.split()
    return len(split_book)

def book_text_char_cnt(input_book):
    book_to_char = (get_book_text(input_book)).lower()
    char_uniq_set = set(book_to_char)
    char_dict = dict.fromkeys(char_uniq_set, 0)

    for i in book_to_char:
        char_dict[i] += 1

    sorted_char_dict = {}

    for key in sorted(char_dict, key=char_dict.get, reverse=True):
        sorted_char_dict[key] = char_dict[key]

    return sorted_char_dict

def sort_on(items):
    return items["num"]