def get_book_text(path_to_file):   
    with open(path_to_file) as f:
        # do something with f (the file) here

        # f is a file object
        file_contents = f.read()
        return file_contents

def get_num_words(path_to_file):
    t = get_book_text(path_to_file)
    list_of_words = t.split()
    num_words = len(list_of_words)
    return num_words

def get_letter_counts(path_to_file):
    counts ={}
    n = 0
    t = get_book_text(path_to_file)
    for i in range(0, len(t)):
        mixed = t[i:i+1:2]
        letter = mixed.lower()
        if letter in counts:
            n = counts[letter]
            n +=1
            counts[letter] = n
        else:
            # we found a new letter
            counts[letter] = 1
    return counts

