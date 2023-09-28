def find_minimum_length_word(input_string):
    words = input_string.split()

    min_length_word = words[0]
    min_length = len(words[0])

    for word in words:
        current_length = len(word)
        if current_length < min_length:
            min_length_word = word
            min_length = current_length
            
    return min_length_word

input_string = input()

minimum_length_word = find_minimum_length_word(input_string)
print(minimum_length_word)