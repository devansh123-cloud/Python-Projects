def main():
    try:
        a = int(input("Hey Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hi I am inside finally")
        print(__name__)

main()
