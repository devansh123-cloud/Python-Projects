vault = {}

while True:
    print("\n🔐 Password Locker")
    print("1. Add Login")
    print("2. Search Login")
    print("3. Edit Login")
    print("4. Delete Login")
    print("5. Show All Logins")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    # 1. Add Login
    if choice == "1":
        website = input("Enter Website: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        vault[website] = {
            "username": username,
            "password": password
        }

        print("✅ Login added successfully!")

    # 2. Search Login
    elif choice == "2":
        website_search = input("Enter Website to search: ")

        if website_search in vault:
            print("🔍 Login Found:")
            print(f"Username: {vault[website_search]['username']}")
            print(f"Password: {vault[website_search]['password']}")
        else:
            print("❌ Login not found.")

    # 3. Edit Login
    elif choice == "3":
        edit_website = input("Enter Website to Edit: ")

        if edit_website in vault:
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")

            vault[edit_website]["username"] = new_username
            vault[edit_website]["password"] = new_password

            print("✅ Login updated successfully!")
        else:
            print("❌ Website not found.")

    # 4. Delete Login
    elif choice == "4":
        delete_login = input("Enter Website to Delete Login: ")

        if delete_login in vault:
            del vault[delete_login]
            print("🗑️ Login deleted successfully!")
        else:
            print("❌ Website not found.")

    # 5. Show All Logins
    elif choice == "5":
        if not vault:
            print("📭 No logins stored yet.")
        else:
            print("📋 All Saved Logins:")
            for site, details in vault.items():
                print(f"\nWebsite: {site}")
                print(f"Username: {details['username']}")
                print(f"Password: {details['password']}")

    # 6. Exit
    elif choice == "6":
        print("👋 Exiting Password Locker. Stay safe!")
        break

    else:
        print("⚠️ Invalid choice. Please enter a number from 1 to 6.")
