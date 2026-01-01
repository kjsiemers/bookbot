from stats import get_num_words, get_letter_counts

path_to_file = "/home/kent/projects/github.com/bookbot/books/frankenstein.txt"
num_words = get_num_words(path_to_file)
print(f"Found {num_words} total words")
counts = get_letter_counts(path_to_file)
for k in counts:
    print(f"'{k}': {counts[k]}")