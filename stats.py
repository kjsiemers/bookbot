def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with f (the file) here

        # f is a file object
        file_contents = f.read()
        return file_contents

def get_num_words():
    path_to_file = "/home/kent/projects/github.com/bookbot/books/frankenstein.txt"
    t = get_book_text(path_to_file)
    list_of_words = t.split()
    num_words = len(list_of_words)
    print(f"Found {num_words} total words")
