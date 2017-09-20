import string

def alphabet_position(letter):
    return string.ascii_lowercase.index(letter.lower())

def rotate_character(char, rot):
    if char.isupper():
        return string.ascii_uppercase[(alphabet_position(char) + rot) % 26]
    elif char.islower():
        return string.ascii_lowercase[(alphabet_position(char) + rot) % 26]
    else:
        return char

def rotate_string(text, rot):
    result = ""
    for c in text:
        result += rotate_character(c, rot)
    return result