a = int(input("Enter a Number :"))
b = int(input("Enter a number : "))

if (b == 0):
    raise ZeroDivisionError("Hey Program is not meant to divide by Zero")

else:
    print(f"The division a/b is {a/b}")