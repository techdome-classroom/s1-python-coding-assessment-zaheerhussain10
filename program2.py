def decode_message(s: str, p: str) -> bool:
    # Initialize two pointers, one for the string and one for the pattern
    i, j = 0, 0
    star_idx = -1  # Stores the last position of the '*'
    match = 0  # Index of the last match after '*' is found
    
    while i < len(s):
        if j < len(p) and (p[j] == s[i] or p[j] == '?'):
            # Match exact characters or '?' that can match any single character
            i += 1
            j += 1
        elif j < len(p) and p[j] == '*':
            # Record the position of '*' and the position in the string where it started matching
            star_idx = j
            match = i
            j += 1
        elif star_idx != -1:
            # Backtrack: the '*' can match more characters
            j = star_idx + 1
            match += 1
            i = match
        else:
            return False
    
    # After the main loop, check if there are remaining '*' in the pattern that can match nothing
    while j < len(p) and p[j] == '*':
        j += 1
    
    # If all characters of the pattern have been matched
    return j == len(p)
