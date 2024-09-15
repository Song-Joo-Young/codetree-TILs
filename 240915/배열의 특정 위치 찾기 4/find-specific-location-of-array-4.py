arr = list(map(int,input().split()))

idx = 0
cnt = 0
Sum = 0

for num in arr:
    if num == 0:
        break
    idx += 1
    
    if num % 2 == 0:
        cnt += 1
        Sum += num

print(f"{cnt} {Sum}")