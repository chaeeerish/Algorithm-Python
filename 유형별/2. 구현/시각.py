n = int(input())

count = 0

for hour in range(0, n+1):
    for minute in range(0, 60):
        for second in range(0, 60):
            if '3' in str(str(hour) + str(minute) + str(second)):
                count += 1

print(count)