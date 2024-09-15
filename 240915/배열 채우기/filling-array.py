arr = list(map(int,input().split()))

idx = len(arr)

for i in range(len(arr)):
    if arr[i] == 0:
        idx = i - 1

while idx >=0:
    print(arr[idx], end=" ")
    idx -= 1