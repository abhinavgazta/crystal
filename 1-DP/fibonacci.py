# fibonnachi series.. 0 1 1 2 3 5 8 13...

def fibonnachie(n):
    dp = [0]*(n+1)
    print("initial dp", dp)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        print("updating dp", dp)
        dp[i] = dp[i-1] + dp[i-2]
    print("the series", dp)

fibonnachie(7)