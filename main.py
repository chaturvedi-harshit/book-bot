def main():
    book_path = "books/frankenstein.txt"
    file_content = get_book(book_path)
    word_count = get_word_count(file_content)
    character_count_dict = get_count_characters(file_content)
    character_count_lst = convert_to_lst_dict(character_count_dict)
    character_count_lst.sort(reverse=True, key=get_sort_key)
    print("--- Begin report of books/frankenstein.txt ---|")
    get_summary(word_count, character_count_lst)


def get_book(path):
    with open(path) as f:
        return f.read()


def get_word_count(text_file):
    words = text_file.split()
    return len(words)


def get_count_characters(text_file):
    character_count_dict = {}
    for char in text_file:
        lowered_char = char.lower()
        if lowered_char not in character_count_dict:
            character_count_dict[lowered_char] = 1
        else:
            character_count_dict[lowered_char] = character_count_dict[lowered_char] + 1
    return character_count_dict


def convert_to_lst_dict(char_dict):
    list_of_char_dicts = []
    for item in char_dict:
        if item.isalpha():
            # print(f"Adding {item} with a count of {char_dict[item]}")
            list_of_char_dicts.append({"char": item, "count": char_dict[item]})
    return list_of_char_dicts


def get_sort_key(dict):
    return dict["count"]


def get_summary(word_count, char_lst):
    # print(f"{word_count} words found in the document")
    print(f"{word_count} words found in the document")
    for item in char_lst:
        print(f"The '{item['char']}' character was found {
              item['count']} times")
    print("--- End report ---")


main()
