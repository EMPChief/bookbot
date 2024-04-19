def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_count = {}
    for char in text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1
    return character_count

def sort_by_frequency(entry):
    return entry["num"]

with open("book.txt") as f:
    book_text = f.read()

print("Number of words in Frankenstein book:", count_words(book_text))
print("Character counts in Frankenstein book:")

character_count = count_characters(book_text)
character_list = [{"character": char, "num": count} for char, count in character_count.items()]
character_list.sort(reverse=True, key=sort_by_frequency)

for entry in character_list:
    print(f"The '{entry['character']}' character was found {entry['num']} times")
