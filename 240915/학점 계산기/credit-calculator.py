n = int(input())

grade = list(map(float, input().split()))
average = round(sum(grade)/len(grade),1)
print(average)
if average > 4.0:
    print("Perfect")
elif average > 3.0:
    print("Good")
else:
    print("Poor")