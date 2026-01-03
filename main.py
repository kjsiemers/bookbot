import sys
from stats import get_num_words, get_letter_counts, sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path_to_file = "/home/kent/projects/github.com/bookbot/" + sys.argv[1]
short_path = sys.argv[1]
num_words = get_num_words(path_to_file)
# print(f"Found {num_words} total words")
counts = get_letter_counts(path_to_file)
# for k in counts:
#     print(f"'{k}': {counts[k]}")
final_list = sort_dict(counts)

# print report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {short_path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for line in final_list:
    if line["char"].isalpha():
        print(f"{line['char']}: {line['num']}")
print("============= END ===============")        