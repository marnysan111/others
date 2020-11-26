def main():
    fizzbazz()

    return

def fizzbazz():
    i = 1
    ans = []
    while i <= 20:
        if i % 3 == 0 and i % 5 == 0:
            ans.append("Fizz Buzz")
            print("Fizz Buzz")
        elif i % 3 == 0:
            ans.append("Fizz")
            print("Fizz")
        elif i % 5 == 0:
            ans.append("Buzz")
            print("Buzz")
        else:
            ans.append(i)
            print(i)
        i += 1
    
    print(ans)
    return





if __name__ == "__main__":
    main()