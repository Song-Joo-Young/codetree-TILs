arr = list(map(int,input().split()))

idx = len(arr)

for i in range(len(arr)):
    if arr[i] == 0:
        idx = i - 1

while True:
    print(arr[idx], end=" ")
    idx -= 1
    if idx == -1:
        break