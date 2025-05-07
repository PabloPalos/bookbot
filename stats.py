def words_in_book(text): # counts words in text
    words_list = text.split()
    count = len(words_list)
    return count

def count_ch(text):
    chars = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def char_dictionary(chars):
    item = []

    for char, count in chars.items():

        char_info = {"char": char, "num": count}

        item.append(char_info)

    def sort_on(chars):
        return chars["num"]
    
    item.sort(reverse=True, key=sort_on)

    return item