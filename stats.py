def number_of_words (contents):
    word_count=contents.split()
    return len(word_count)


def character_count (contents):
    contents=contents.lower()
    char_count={}
    for char in contents:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1

    
    return char_count


def sort_on(items):
    return items["num"]

def sort_character_counts(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_list.append({"char": char, "num": count})

    # Sort the list by count, from highest to lowest
    sorted_list.sort(reverse=True, key=sort_on)    
    return sorted_list





