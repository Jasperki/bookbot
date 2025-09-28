import sys
from stats import get_num_words, get_num_chars, get_num_chars_sorted

def main():
    # book_path = 'books/frankenstein.txt'
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("------- Character Count ---------")
        character_statistics = get_num_chars(book_text)
        character_statistics_sorted = get_num_chars_sorted(character_statistics)
        for item in character_statistics_sorted:
            print(f"{item['char']}: {item['num']}")
    
def get_book_text(book):
    with open(book) as b:
        text = b.read()
    return text

main()
