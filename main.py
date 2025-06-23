import sys
from stats import count_words, count_characters, sort_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

FILE_PATH = sys.argv[1]

try:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"Error: File not found at '{FILE_PATH}'")
    sys.exit(1)

word_count = count_words(text)
character_count = count_characters(text)
sorted_characters = sort_characters(character_count)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {FILE_PATH}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for char, count in sorted_characters[:5]:
    print(f"{char}: {count}")
