def main():
    book_to_read = "books/frankenstein.txt"
    book_text = get_book_text(book_to_read)
    book_word_count = get_word_count(book_text)
    book_char_dict = count_characters(book_text)
    

    #print (book_text)
    print(f"word count: {book_word_count}")
    print(f"character count: {book_char_dict}")

def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_characters = text.lower()
    characters_count = {}

    for char in lowered_characters:
        if char in characters_count:
            characters_count[char] += 1
        else:
            characters_count[char] = 1
    return characters_count

main()



    #lowered_characters = text.lower()
    #character_split = lowered_characters.split()
    #return len(lowered_characters)
#    
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