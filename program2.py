def decode_message(secret_message, pattern):
    """
    Determines if a secret message matches a given pattern with wildcards.

    Args:
        secret_message: The secret message to match.
        pattern: The pattern to match against.

    Returns:
        True if the pattern matches the secret message, False otherwise.
    """

    m = len(secret_message)
    n = len(pattern)

    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = True

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '?' or secret_message[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[m][n]