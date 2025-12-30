def get_book_text(file_path):
    try:
        with open(file_path) as f:
            return f.read()
            
    except FileNotFoundError:
        print(f"Error: File at {file_path} not found.")
        return None

def book_text_word_cnt(input_book):
    split_book = input_book.split()
    return len(split_book)

def book_text_char_cnt(input_book):
    book_to_char = input_book.lower()
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