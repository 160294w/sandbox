# https://atcoder.jp/contests/dp/tasks/dp_a
N = int(input())
cost_one = 0
#ost_two = 0
dp = [float('inf')] * N

cost_one = list((map(int,(input().split()))))
#print(cost_one)
#cost_two = (input().split())
#print(cost_one)
#print(cost_two)
for i in range(2,N-1):
    print(cost_one[i-2] - cost_one[i])
    print(cost_one[i-1] - cost_one[i])
    print("ho")
    dp[i] = min(abs(cost_one[i-2] - cost_one[i]), abs(cost_one[i-1] - cost_one[i]))

print(dp)
