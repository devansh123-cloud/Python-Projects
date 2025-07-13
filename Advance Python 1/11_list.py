# myList = [1,2,3,4,5,6]
# squaredList = [i*i for i in myList]
# print(squaredList)

def square(n: int) -> int:
    return n * n

# Step 1: Ask user for input
num = int(input("Enter a number: "))  # Don't call the function here

# Step 2: Call the function with user's input
result = square(num)

# Step 3: Print the result
print(f"The square of {num} is {result}")
