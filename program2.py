def decode_message(s: str, p: str) -> bool:
    # Use two pointers to iterate through the string and pattern
    i, j = 0, 0
    star_idx = -1  # To remember the position of '*' in pattern
    match = 0  # To remember the index of the string that matches a '*' in the pattern

    while i < len(s):
        if j < len(p) and (p[j] == s[i] or p[j] == '?'):
            # If the current characters match or the pattern has a '?'
            i += 1
            j += 1
        elif j < len(p) and p[j] == '*':
            # If there's a '*' in the pattern, we remember the position and try matching the rest
            star_idx = j
            match = i
            j += 1
        elif star_idx != -1:
            # If there's no direct match and we had a previous '*', we try to match further
            j = star_idx + 1
            match += 1
            i = match
        else:
            return False

    # After finishing the string, check for remaining '*' in the pattern
    while j < len(p) and p[j] == '*':
        j += 1

    return j == len(p)

