def main():
    print("let's read a book")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

main()
