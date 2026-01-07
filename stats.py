def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def character(text):
    s_t={}
    for i in text:
        i=i.lower()
        if i not in s_t:
           s_t[i] = 1
        else:
           s_t[i] += 1
    return s_t

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    char_words = character(text)
    print(char_words)

main()

