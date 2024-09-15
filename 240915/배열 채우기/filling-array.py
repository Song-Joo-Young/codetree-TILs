arr = list(map(int,input().split()))
# arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 33]

idx = len(arr)

for i in range(len(arr)):
    if arr[i] == 0:
        idx = i-1

if idx != len(arr):
    for _ in range(idx+1):
        print(arr[idx], end=" ")
        idx -= 1
else:
    for i in range(len(arr)):
        print(arr[len(arr)-1-i], end=" ")