

def match(pattern, string):
    """
    Pattern Matching

    Take an input `pattern` and an input `string` and determine if they match. Pattern may use
    the following special characters:

      * = match against 0 or more arbitrary characters
      ! = match a single arbitrary character

    """

    if pattern is None or string is None:
        return False
    if pattern == string == '':
        return True

    size_s = len(string)
    size_p = len(pattern)
    dp = [[False for _ in range(size_s + 1)] for _ in range(size_p + 1)]
    dp[0][0] = True

    for i in range(1, size_p + 1):
        if pattern[i - 1].isalpha() or pattern[i - 1] == '!':
            dp[i][0] = False
        else:
            if i >= 2:
                dp[i][0] = dp[i - 2][0]

    for row in range(1, size_p + 1):
        for col in range(1, size_s + 1):
            # 0....size
            i = row - 1
            j = col - 1

            if pattern[i].isalpha():
                if pattern[i] == string[j]:
                    dp[row][col] = dp[row - 1][col - 1]
            elif pattern[i] == '!':
                dp[row][col] = dp[row - 1][col - 1]
            else:
                if i - 1 >= 0 and (pattern[i - 1] == '!' or pattern[i - 1] == string[j]):
                    if row - 2 >= 0:
                        dp[row][col] = dp[row - 2][col] or dp[row][col - 1]
                    else:
                        dp[row][col] = dp[row][col - 1]
                elif row - 2 >= 0:
                    dp[row][col] = dp[row - 2][col]

    # print(dp)
    return dp[-1][-1]
