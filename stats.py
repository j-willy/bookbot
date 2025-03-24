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

def sort_on(dict):
    return dict["count"]

def sorting_fucntion(char_dict):
    sorted_count = []
    for char in char_dict:
        count = char_dict[char]
        sorted_count.append({"char": char, "count": count})
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count