def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = count_words(book)
    print(f"{word_count} words found in the document")
    
def get_book_text(filepath):
   with open(filepath) as file:
        return file.read()

def count_words(book):
    words = book.split()
    return len(words)

main()