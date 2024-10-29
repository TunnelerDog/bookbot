def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    words = get_word_count(text)
    print(f"Word Count: {words}")
    character_count = get_letter_count(text)
    print(character_count)
    sorted_character_count = sort_dict(character_count)
    print_report(book_path, words, sorted_character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    lowered_string = text.lower()
    # read each character and add to dictionary
    letter_count = {}
    for character in lowered_string:
        if character in letter_count:
            value = letter_count[character]
            value += 1
            letter_count.update({character:value})
        else:
            letter_count.update({character:1})
    return letter_count

def sort_dict(dict):
    sorted_list = sorted(dict.items(), key=lambda item:item[1], reverse=True)
    sorted_dict = {}
    for key, value in sorted_list:
        sorted_dict[key] = value
    return sorted_dict

def print_report(file, words, characters):
    print(f"--- Begin report of {file} ---")
    print(f"{words} words are found in the documnet")
    print("")
    alpha_char = {}
    for character in characters:
        if character.isalpha():
            print(f"The '{character}' character was found {characters[character]} times")


main()