def myfunction():
    print("Helo ")

def myclass():
    print("Bonjour Howdy ")
    print(__name__)  # Will show __main__ or filename

# This block runs only if you run this file directly (not on import)
if __name__ == "__main__":
    print("We are here")
    myfunction()
    print(__name__)  # Will print __main__

# This line will always run, even when imported
myclass()
