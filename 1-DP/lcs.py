def longest_common_subsequence(str1, str2):
    """
    Finds the length of the longest common subsequence (LCS) of two strings using dynamic programming.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        The length of the LCS.

DP TABLE>>....
         ""  G  X  T  X  A  Y  B
   ""  0  0  0  0  0  0  0  0
   A   0  0  0  0  0  1  1  1
   G   0  1  1  1  1  1  1  1
   G   0  1  1  1  1  1  1  1
   T   0  1  1  2  2  2  2  2
   A   0  1  1  2  2  3  3  3
   B   0  1  1  2  2  3  3  4-> ans....
    """

    m = len(str1)
    n = len(str2)

    # Create a 2D array (dp) to store the lengths of LCS for subproblems.
    # dp[i][j] stores the length of the LCS of str1[0...i-1] and str2[0...j-1].
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table in bottom-up manner.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # If characters match, increment the LCS length from the diagonal element.
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If characters don't match, take the maximum LCS length from the top or left element.
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The bottom-right element of the dp table contains the length of the LCS of the entire strings.
    return dp[m][n]

# Example usage:
str1 = "AGGTAB"
str2 = "GXTXAYB"
lcs_length = longest_common_subsequence(str1, str2)
print(f"Length of LCS: {lcs_length}")  # Output: 4 $ GTAB....