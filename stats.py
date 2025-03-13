def count_words(book):
    words = book.split()
    return len(words)

def count_letters(text):
    char_counts = {}
    for character in text:
        character = character.lower()
        if character not in char_counts:
            char_counts[character] = 1
        else:
            char_counts[character] += 1
    return char_counts
