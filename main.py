

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with f (the file) here

        # f is a file object
        file_contents = f.read()
        return file_contents

def main():
    path_to_file = "/home/kent/projects/github.com/bookbot/books/frankenstein.txt"
    t = get_book_text(path_to_file)
    print(t)

main()