def main():
    #path to book and adding the book to text
    book_to_read = "books/frankenstein.txt"
    book_text = get_book_text(book_to_read)
    
    #getting the word count
    book_word_count = get_word_count(book_text)
    
    #functions to generate the character dictionary
    book_char_dict = count_characters(book_text)
    
    #converting dictionary into a list of dictionaries by char
    book_char_list = char_list(book_char_dict)

    ##print (book_text)
    #printing the report
    print(f"--- Begin report of {book_to_read} ---")
    print(f"{book_word_count} words found in the document")
    ##print(f"character count: {book_char_dict}")

    #printing the char list sorted

    book_char_list.sort(reverse=True, key=sort_on)

    for char in book_char_list:
        print(f"The '{char['char']}' character was found {char['count']} times")

#sorting the list of dictionaries and printing sorted char list
    
def char_list(list):
    charlist = []
    for char, count in list.items():
        if char.isalpha():
            charlist.append({"char": char, "count": count})
    return charlist

def sort_on(dict):
    return dict["count"]

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