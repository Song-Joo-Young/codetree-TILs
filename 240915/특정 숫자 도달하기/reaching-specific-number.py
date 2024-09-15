arr = list(map(int, input().split()))

Sum = 0
count = 0

for num in arr:
    if num < 250:
        Sum += num
        count += 1
    else:
        break

print(f"{Sum} {round(Sum/count,1)}")