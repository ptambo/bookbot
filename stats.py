def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    text = text.lower()
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def dict_to_list(dict):
    result = []
    for item in dict:
        if item.isalpha():
            result.append({"char": item, "num": dict[item]})
    return result

def sort_on(items):
    return items["num"]