def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars_stats = {}
    for char in text:
        c = char.lower()
        if c in chars_stats:
            chars_stats[c] += 1
        else:
            chars_stats[c] = 1
    return chars_stats

def sort_on(items):
    return items['num']

def get_num_chars_sorted(char_stats):
    char_list = []
    for char in char_stats:
        if char.isalpha():
            count = char_stats[char]
            char_list.append({'char': char, 'num': count})
    return sorted(char_list, reverse=True, key=sort_on)