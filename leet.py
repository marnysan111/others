input_line = input()

ans = ""
for i in input_line:
    if i == "A":
        ans += "4"
    elif i == "E":
        ans += "3"
    elif i == "G":
        ans += "6"
    elif i == "I":
        ans += "1"
    elif i == "O":
        ans += "0"
    elif i == "S":
        ans += "5"
    elif i == "Z":
        ans += "2"
    else:
        ans += i


print(ans)