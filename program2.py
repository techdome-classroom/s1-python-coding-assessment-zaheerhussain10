def decode_message(secret_message, pattern):
    # Get the lengths of both secret_message and pattern
    m = len(secret_message)
    n = len(pattern)
    
    # Create a 2D dp table where dp[i][j] represents if
    # the first i characters of secret_message match the first j characters of pattern
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty secret_message matches an empty pattern
    dp[0][0] = True
    
    # If the pattern starts with '*' or has continuous '*' symbols,
    # it can match an empty secret_message.
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == secret_message[i - 1] or pattern[j - 1] == '?':
                # Characters match or '?' matches any character
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                # '*' can match an empty sequence or any sequence of characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    # The result is whether the entire secret_message matches the entire pattern
    return dp[m][n]

