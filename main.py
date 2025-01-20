def main():
    book_to_read = "books/frankenstein.txt"
    book_text = get_book_text(book_to_read)
    book_word_count = get_word_count(book_text)

    print (book_text)
    print(f"word count: {book_word_count}")

def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

main()




#def main():
#    book_to_read = "books/frankenstein.txt"
#    with open(book_to_read) as f:
#        book_text = f.read()
#    print(book_text)
#
#    words = book_text.split()
#    word_count = len(words)
#    print(word_count)
#
#main()