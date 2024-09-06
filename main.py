def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowercased_text = text.lower()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    characters_dict = get_num_characters(lowercased_text)
    sl = sort_on(characters_dict)
    sl.sort(key=get_count, reverse=True)

    for item in sl:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['count']} times")

    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
        #lit l'emsemble de frankenstein.txt

def get_num_words(text):
    words = text.split()
    #découpe le livre avec chaque mot = un string
    return len(words) 

def get_num_characters(text):
    characters_num = {}
    for character in text:
        if character in characters_num:
            characters_num[character] += 1
            #Incrémente la clé de 1 
        else: 
            characters_num[character] = 1
            #définis la permiére clé = 1
    return characters_num

def sort_on(dictio):
    sorted_list =[]
    for char, count in dictio.items():
        sorted_list.append({"char": char, "count": count})
    return sorted_list

def get_count(dict):
    return dict["count"]

    





"""
    words_number = 0
    for word in words:
        words_number += 1
    print(words_number)
    #Incrément pour chaques mots dans le split words """

"""def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

    word_count = len(words)
    print(word_count)

main()
"""

main()