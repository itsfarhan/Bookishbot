#Function to get in path and read file.
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Function to get number of words in text file
def num_of_words(text):
    words = text.split()
    return len(words)

#Function to get text in character (lower format)
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#sorting function
def sort_on(d):
    return d["num"]

#characters sorting function
def chars_dict_sorted(num_chars_dicts):
    sorted_list = []
    for ch in num_chars_dicts:
        sorted_list.append({"char": ch, "num":num_chars_dicts[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

#main function
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) #/path/to/the/file
    num = num_of_words(text) ##number of words in file.
    chars_dict = get_chars_dict(text) #characters in dictionary
    chars_sorted_list = chars_dict_sorted(chars_dict) #sorting dictionary
    
    print(f"------->Begin report of Frankenstein<-------")
    print(f"{num} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha(): #if text in file is char or numerical. if character then continue.
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    print("--->End Report<---")

main()