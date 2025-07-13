# 📚 Library Book Manager
# 1. Add Book
# 2. Search Book
# 3. Edit Book
# 4. Delete Book
# 5. Show All Books
# 6. Exit

# Enter your choice: 1
# Enter Book ID: B101
# Enter Title: Atomic Habits
# Enter Author: James Clear
# Enter Genre: Self-Help
# ✅ Book added successfully!

books = {}

while True: 
    print("\n 📚 Library Book Manager")
    print("1. Add Book")
    print("2.Search Book")
    print("3. Edit Book")
    print("4. Delete Book")
    print("5. Show All Books")
    print("6. Exit")
    
    choice = input("Enter your choice : ")
    
    if choice == "1":
        book_id = input("Enter Book ID:")
        title = input("Enter Book Title:")
        author_name = input("Enter Author Name:")
        genre = input("Enter your Genre : ")
        
        books[book_id] = {
         
            "title" : title,
            "author_name" : author_name,
            "genre" : genre
        }
        
        print("✅ Book added successfully!")
    
    elif choice == "2":
        search_book = input("Enter ID to search Book : ")
        
        if search_book in books : 
            print("📖 Book Found:")
            print(f"Title:{books[search_book]['title']}")
            print(f"Author Name : {books[search_book]['auhor_name']}")
            print(f"Genre: {books[book_id][genre]}")
           
        else : 
            print("❌ Book not found.")
            
            
    
    elif choice == "3":
        edit_ID = input("Enter BOOK ID to EDIT :")
        if edit_ID in books : 
            new_title = input("Enter NEW TITLE:")
            new_author = input("Enter NEW AUTHOR:")
            new_genre = input("Enter NEW GENRE :")
            
            books[edit_ID]['title'] = new_title
            books[edit_ID]['author_name'] = new_author
            books[edit_ID]['genre'] = new_genre
            
            print("✅ Book updated successfully!")
            
        else :
            print("❌ Book ID not found")
        
        
    elif choice == "4":
        
        delete_book = input("Enter BOOK ID to DELETE BOOK")
        if delete_book in books:
            del books[book_id]
            print("🗑️ Book deleted.")
        else:
            print("❌ Book not found.")
            
            # Show All Books
    elif choice == "5":
        if not books:
            print("📭 No books found in the system.")
        else:
            print("📚 All Books:")
            for book_id, book_info in books.items():
                print(f"\nID: {book_id}")
                print(f"Title: {book_info['title']}")
                print(f"Author: {book_info['author_name']}")
                print(f"Genre: {book_info['genre']}")

    # Exit
    elif choice == "6":
        print("👋 Exiting Library Book Manager. Goodbye!")
        break

    else:
        print("❗ Invalid choice. Please enter a number from 1 to 6.")
                

            
            
        
        
        