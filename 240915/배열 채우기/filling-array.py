arr = list(map(int,input().split()))

idx = len(arr)

for i in range(len(arr)):
    if arr[i] == 0:
        idx = i-1

if idx != len(arr):
    for _ in range(idx+1):
        print(arr[idx], end=" ")
        idx -= 1
else:
    for _ in range(idx):
        print(arr[idx], end=" ")
        idx -= 1