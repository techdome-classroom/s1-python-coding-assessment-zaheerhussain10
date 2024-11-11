def decode_message(s: str, p: str) -> bool:
    # Create a memoization table to store results for subproblems
    memo = {}

    def dp(i, j):
        # If we have already computed this state, return its result
        if (i, j) in memo:
            return memo[(i, j)]
        
        # If the pattern is exhausted, check if the string is also exhausted
        if j == len(p):
            return i == len(s)
        
        # If the string is exhausted but pattern is not
        if i == len(s):
            # The pattern must only contain '*' for it to match
            return all(x == '*' for x in p[j:])
        
        # Match the current character
        if p[j] == s[i] or p[j] == '?':
            result = dp(i + 1, j + 1)
        elif p[j] == '*':
            # Try to match the '*' with different lengths (from 0 to the remaining string length)
            result = dp(i, j + 1) or dp(i + 1, j)
        else:
            result = False
        
        # Memoize the result
        memo[(i, j)] = result
        return result

    return dp(0, 0)

