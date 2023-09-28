def writeAsYouSpeak(n):
    if n <= 0:
        return ""
    
    sequence = "1"
    
    for _ in range(n - 1):
        new_sequence = ""
        count = 1
        current_digit = sequence[0]
        
        for i in range(1, len(sequence)):
            if sequence[i] == current_digit:
                count += 1
            else:
                new_sequence += str(count) + current_digit
                count = 1
                current_digit = sequence[i]
        
        new_sequence += str(count) + current_digit
        sequence = new_sequence
    
    return sequence