import sys
from stats import get_num_words, dict_list

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def sort_on(text):
    return text["num"]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        text_dict = dict_list(book_text)
        num_words = get_num_words(book_text.split())
        print("============ BOOKBOT ============")
        print(f'Analyzing book found at {sys.argv[1]}...')
        print("------------ Word Count ------------")
        print(f'Found {num_words} total words')
        print("------------ Character Count ------------")
        for d in text_dict:
            print(f'{d["char"]}: {d["num"]}')

        print("============ END ============")


main()
    
