n = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0
for _ in range(n):
    shift = list(input().split())
    if shift[0] == 'E':
        DIR = 0
    elif shift[0] == 'S':
        DIR = 1
    elif shift[0] == 'W':
        DIR = 2
    else:
        DIR = 3
    x = x + int(shift[1]) * dx[DIR]
    y = y + int(shift[1]) * dy[DIR]

print(f"{x} {y}")