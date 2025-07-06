


def get_num_words(path_to_file):
    text = get_book_text(path_to_file)
    text = text.split(" ")

    print(f"number of characters: {len(text)}")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def sort_on_numbers(items):
    return items["num"]

def count_characters(path_to_file):
    text = get_book_text(path_to_file)
    char_count = {}
    list_char_count = []
    for i in text:
        if i.isalnum():
            if i.lower() in char_count:
                char_count[i.lower()] += 1
            else:
                char_count[i.lower()] = 1

    for i in char_count:
        list_char_count.append({"char":i, "num":char_count[i]})


    return sorted(list_char_count, key=sort_on_numbers,reverse=True)

    
    

