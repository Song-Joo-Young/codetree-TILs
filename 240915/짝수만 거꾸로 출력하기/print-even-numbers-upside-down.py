n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[n-1-i] % 2 == 0:
        print(arr[n-1-i], end = " ")