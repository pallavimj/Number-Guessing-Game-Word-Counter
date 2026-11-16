
from collections import Counter
import string

print("================================")
print("       WORD COUNTER TOOL")
print("================================")

filename = input("Enter text file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    for char in string.punctuation:
        text = text.replace(char, "")

    # Split text into words
    words = text.split()

    # Count total words
    total_words = len(words)

    # Count unique words
    unique_words = len(set(words))

    # Calculate word frequency
    frequency = Counter(words)

    print("\n========== RESULTS ==========")
    print("Total words:", total_words)
    print("Unique words:", unique_words)

    print("\nWord Frequency:")

    for word, count in frequency.most_common():
        print(f"{word}: {count}")

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")