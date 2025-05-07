import sys
from stats import words_in_book
from stats import count_ch
from stats import char_dictionary


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def get_book_text(path_to_book): # Declares function that takes a file path as an input

    with open(path_to_book) as f: # Opens the file safely, Python will close it when finished
        file_contents = f.read() # f.read() reads entire file's contents into a string
                                 # Assign that string to file_contents
                                   

    return file_contents #Sends string back out of the function


def main(): # Defines main() with no inputs
    text = get_book_text(path_to_book) # Calls get_book_text with relative path to your book, stores the result in text
    count = words_in_book(text)
    char_counts = count_ch(text)

    # print(f"{count} words found in the document")
    # print(f"{lowercase}")

    sorted_chars = char_dictionary(char_counts)

    print("=========BOOKBOT===========")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count -----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")



main()

