def decode_message(s: str, p: str) -> bool:
    i, j = 0, 0
    star_idx = -1  # Position of '*' in pattern
    match = 0  # Position to match in the string after '*' in pattern

    while i < len(s):
        if j < len(p) and (p[j] == s[i] or p[j] == '?'):
            # If the current characters match or the pattern has a '?'
            i += 1
            j += 1
        elif j < len(p) and p[j] == '*':
            # If there's a '*' in the pattern, we record its position and try to match the rest
            star_idx = j
            match = i
            j += 1
        elif star_idx != -1:
            # If we had a '*' before, we try to match more characters from string
            j = star_idx + 1
            match += 1
            i = match
        else:
            return False

    # If there's any remaining '*' in the pattern, we move the pointer
    while j < len(p) and p[j] == '*':
        j += 1

    return j == len(p)  # Return True if we have matched the whole pattern
