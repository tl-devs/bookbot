def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()

    return file_content

def main():
    test_file_path = "books/frankenstein.txt"
    print(get_book_text(test_file_path))

main()
