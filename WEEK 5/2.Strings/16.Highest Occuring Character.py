def highestOccuringChar(string):
    ASCII_SIZE = 256
    ctr = [0] * ASCII_SIZE
    max_count = -1
    most_frequent_char = ''

    for char in string:
        ctr[ord(char)] += 1

    for char in string:
        if ctr[ord(char)] > max_count:
            max_count = ctr[ord(char)]
            most_frequent_char = char

    return most_frequent_char
