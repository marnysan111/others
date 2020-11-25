# https://paiza.jp/student/challenges/413/retry

input_line = input()
i = int(input_line)
count = 1
check = 0
d1 = 0
num = 0
a = True
ans = 0

while a == True:
    if i == num or i == 0:
        a = False
        d1 -= abs(check)
    else:
        if (count % 2) == 0 and count != 0:
            check = check * -1
        else:
            check = abs(check) + 1
        num = check
        d1 += abs(check) * 2
        count += 1

count = 1
check = 0
d2 = 0
num = 0
a = True
ans = 0
m = 0
while a == True:
    if abs(i) < abs(num) or i == 0:
        a = False
        if i < 0:
            d2 = d2 + (check * 2)
        elif i > 0:
            d2 = d2 + i
    else:
        if (count % 2) == 0 and count != 0:
            check = check * -1
        else:
            check = 2 ** m
            m += 1
        num = check
        d2 += count
        count += 1

print(d1, d2)

