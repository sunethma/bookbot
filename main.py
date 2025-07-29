from stats import number_of_words,character_count,sort_character_counts
import sys

def get_book_text (path):
    with open(path,encoding="utf-8") as f:
        file_contents=f.read()
        return number_of_words(file_contents),character_count(file_contents)
    



def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    words_count,char_count=get_book_text (book_path)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------")
    print("Found "+str(words_count) + " total words "+"\n--------- Character Count -------")
    sorted_character=sort_character_counts(char_count)
    for item in sorted_character:
        print (f"{item['char']}: {item['num']}")
    print("============= END ===============")



main()




