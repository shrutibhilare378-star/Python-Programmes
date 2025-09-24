undo_stack = []
redo_stack = []

def make_change():
    text = input("Enter new content: ")
    undo_stack.append(text)
    redo_stack.clear()

def undo():
    if undo_stack:
        X = undo_stack.pop()
        redo_stack.append(X)
    else:
        print("Nothing to undo.")

def redo():
    if redo_stack:
        X = redo_stack.pop()
        undo_stack.append(X)
    else:
        print("Nothing to redo.")

def display():
    print("\nCurrent document content:")
    for i in undo_stack:
        print(i, end="")
    print("\n")

while True:
    print("Text editor menu")
    print("1. Make a change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display document")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        make_change()
        display()
    elif choice == "2":
        undo()
        display()
    elif choice == "3":
        redo()
        display()
    elif choice == "4":
        display()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")

