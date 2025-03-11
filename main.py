def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    words = []
    counter = 0
    book = get_book_text("books/frankenstein.txt") 
    words = book.split()
    
    for word in words:
        counter += 1
    print(f"{counter} words found in the document")
main()