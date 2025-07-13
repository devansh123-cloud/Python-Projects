def greet(name):
    return f"Hello, {name}! 👋"

def farewell(name):
    return f"Goodbye, {name}! 👋"

# Test block (won't run when imported)
if __name__ == "__main__":
    print("📦 Running greeter module directly")
    print(greet("Devansh"))
    print(farewell("Devansh"))
