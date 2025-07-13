password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()-_+=<>?/|{}[]~"

if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("✅ Strong password!")
    else:
        print("⚠️ Weak password. Missing:")
        if not has_upper:
            print("- Uppercase letter")
        if not has_lower:
            print("- Lowercase letter")
        if not has_digit:
            print("- Digit")
        if not has_special:
            print("- Special character")
else:
    print("❌ Password must be at least 8 characters long.")
