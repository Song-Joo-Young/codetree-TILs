arr = list(map(int,input().split()))

idx = len(arr)

for i in range(len(arr)):
    if arr[i] == 0:
        idx = i - 1

for j in range(idx):
    print(arr[idx-j], end=" ")