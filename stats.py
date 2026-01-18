def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_chars_dict(text):
    s_t={}
    for i in text:
        i=i.lower()
        if i not in s_t:
           s_t[i] = 1
        else:
           s_t[i] += 1
    return s_t

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    book = sys.argv
    text = get_book_text(book)
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    char_words = get_chars_dict(text)
    char_words=chars_dict_to_sorted_list(char_words)
    print("------- Character Count ---------")
    for i in char_words:
        if i["char"].isalpha() == True:
            print(f'{i["char"]}: {i["num"]}')
    print("============= END ===============")
    print(sys.argv)
def chars_dict_to_sorted_list(s_t):
    item=[]
    for i in s_t:
        item.append({"char":i,"num":s_t[i]})
    item.sort(reverse=True, key=sort_on)
    return item

def sort_on(item):
    return item["num"]

main()