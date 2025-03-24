from stats import count_words, count_letters, sorting_fucntion
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_count = count_words(book)
    char_dict = count_letters(book)
    sorted_chars = sorting_fucntion(char_dict)
    formating(book_path,word_count,sorted_chars)

def get_book_text(filepath):
   with open(filepath) as file:
        return file.read()

def formating(book_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
        
main()