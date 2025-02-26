import sys

from stats import count_words, count_chars, sort_char_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # Get the text
    book_text = get_book_text(sys.argv[1])
    
    # Get counts
    word_count = count_words(book_text)
    char_counts = count_chars(book_text)
    sorted_chars = sort_char_dict(char_counts)

    # Print report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = next(iter(char_dict))
        count = char_dict[char]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()