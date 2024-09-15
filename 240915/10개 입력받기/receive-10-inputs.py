arr = list(map(int,input().split()))

idx = 0
Sum = 0

for num in arr:
    if num == 0:
        break
    idx += 1
    Sum += num

print(f"{Sum} {round(Sum/idx,1)}")