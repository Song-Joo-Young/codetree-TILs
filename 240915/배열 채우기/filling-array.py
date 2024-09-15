arr = list(map(int,input().split()))

idx = len(arr)

for i in range(len(arr)):
    if arr[i] == 0:
        idx = i-1


for _ in range(idx+1):
    print(arr[idx], end=" ")
    idx -= 1