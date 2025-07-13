books = {}

while True:
    print("\n📚 Library Book Manager")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Edit Book")
    print("4. Delete Book")
    print("5. Show All Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author_name = input("Enter Author Name: ")
        genre = input("Enter Genre: ")

        books[book_id] = {
            "title": title,
            "author_name": author_name,
            "genre": genre
        }

        print("✅ Book added successfully!")

    elif choice == "2":
        search_id = input("Enter Book ID to search: ")

        if search_id in books:
            print("📖 Book Found:")
            print(f"Title: {books[search_id]['title']}")
            print(f"Author Name: {books[search_id]['author_name']}")
            print(f"Genre: {books[search_id]['genre']}")
        else:
            print("❌ Book not found.")

    elif choice == "3":
        edit_id = input("Enter Book ID to edit: ")

        if edit_id in books:
            new_title = input("Enter NEW TITLE: ")
            new_author = input("Enter NEW AUTHOR: ")
            new_genre = input("Enter NEW GENRE: ")

            books[edit_id]["title"] = new_title
            books[edit_id]["author_name"] = new_author
            books[edit_id]["genre"] = new_genre

            print("✅ Book updated successfully!")
        else:
            print("❌ Book ID not found.")

    elif choice == "4":
        del_id = input("Enter Book ID to delete: ")

        if del_id in books:
            del books[del_id]
            print("🗑️ Book deleted successfully!")
        else:
            print("❌ Book ID not found.")

    elif choice == "5":
        if not books:
            print("📭 No books in the library.")
        else:
            print("📚 All Books:")
            for book_id, info in books.items():
                print(f"\nID: {book_id}")
                print(f"Title: {info['title']}")
                print(f"Author: {info['author_name']}")
                print(f"Genre: {info['genre']}")
    elif choice == "6":
        print("👋 Exiting the program.")
        break

    else:
        print("⚠️ Invalid choice. Please enter a number from 1 to 6.")
