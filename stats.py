# Number of words function
def count_words(book_text):
    words = book_text .split()
    number_of_words = len(words)
    return number_of_words

def count_chars(text):
    char_counts = {} # Empty Dictionary
    lowered_text = text.lower() # Convert all characters to lowercase first

    for char in lowered_text:
        if char in char_counts:
	        char_counts[char] +=1
        else:
            char_counts[char] = 1
    
    return char_counts # this is required

def sort_on(dict):
    return list(dict.values())[0]

def sort_char_dict(char_counts):
    chars_list = []
    for character, count in char_counts.items():
        char_dict = {character: count}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on) 
    return chars_list
