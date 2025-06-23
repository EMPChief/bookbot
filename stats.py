def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower_text = text.lower()
    character_count = {}
    for char in lower_text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1
    return character_count


def sort_characters(char_counts):
    return sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
