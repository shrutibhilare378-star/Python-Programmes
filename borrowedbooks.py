member_borrow_counts = {}
book_borrow_counts = {}

# Borrowing function
def borrow_book(member_id, book_title):
    member_borrow_counts[member_id] = member_borrow_counts.get(member_id, 0) + 1
    book_borrow_counts[book_title] = book_borrow_counts.get(book_title, 0) + 1

# Average books borrowed
def average_books_borrowed():
    total = sum(member_borrow_counts.values())
    count = len(member_borrow_counts)
    return total / count if count > 0 else 0

# Highest and lowest borrowed books
def book_with_highest_and_lowest_borrowings():
    if not book_borrow_counts:
        return None, None
    max_book = max(book_borrow_counts, key=book_borrow_counts.get)
    min_book = min(book_borrow_counts, key=book_borrow_counts.get)
    return max_book, min_book

# Count members with zero borrowings
def count_members_with_zero_borrowings(all_members):
    return sum(1 for member in all_members if member_borrow_counts.get(member, 0) == 0)

# Most frequently borrowed book(s)
def most_frequently_borrowed_book():
    if not book_borrow_counts:
        return None
    max_count = max(book_borrow_counts.values())
    return [book for book, count in book_borrow_counts.items() if count == max_count]

# Main program
def main():
    all_members = set()
    print("Library Borrowing System")
    while True:
        print("\nChoose an option:")
        print("1. Borrow a book")
        print("2. Show average books borrowed")
        print("3. Show most and least borrowed books")
        print("4. Count members with zero borrowings")
        print("5. Show most frequently borrowed book(s)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            member_id = input("Enter member ID: ")
            book_title = input("Enter book title: ")
            borrow_book(member_id, book_title)
            all_members.add(member_id)
            print(f"{member_id} borrowed '{book_title}'")
        elif choice == "2":
            avg = average_books_borrowed()
            print(f"Average books borrowed: {avg:.2f}")
        elif choice == "3":
            high, low = book_with_highest_and_lowest_borrowings()
            print(f"Most borrowed book: {high}")
            print(f"Least borrowed book: {low}")
        elif choice == "4":
            total_members = input("Enter all member IDs separated by commas: ").split(",")
            total_members = [m.strip() for m in total_members]
            count = count_members_with_zero_borrowings(total_members)
            print(f"Members with zero borrowings: {count}")
        elif choice == "5":
            mode_books = most_frequently_borrowed_book()
            if mode_books:
                print("Most frequently borrowed book(s):", ", ".join(mode_books))
            else:
                print("No books have been borrowed yet.")
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

