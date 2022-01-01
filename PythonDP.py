# 파이썬 1463번 문제 
n = int(input())

dp = [0] * (n+1) # +1을 해주는 이유는 배열의 인덱스가 0부터 시작하므로 for문의 i를 이용한 dp[i]번쨰를 꺼낼때 순서가 맞지 않으므로 +1을 해주는 것 같다.

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])