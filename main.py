import sys
from stats import word_counter,character_counter,sort_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    
    if len(sys.argv) < 2:
        print("Error: No file path provided. Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    book = get_book_text(path_to_file)
    word_count = word_counter(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_dict = character_counter(book)
    sorted_chars = sorted(character_dict.items(), key = sort_chars, reverse = True)
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("============= END ===============")
    

main()