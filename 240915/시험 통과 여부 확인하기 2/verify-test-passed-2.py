n = int(input())

cnt = 0

for _ in range(n):
    grade = list(map(int, input().split()))
    avg = sum(grade)/4
    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)