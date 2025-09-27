def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if  choice == 1:
            choices = input("Enter item to add:")
            shopping_list.append(choices)
            print(f"{choices} added to list")
            pass
        elif choice == 2:
            choices = input("Enter item to remove: ")
            shopping_list.remove(choices)
            print(f"{choices} has been removed from your list")
            pass
        elif choice == 3:
            print(f"Your shopping list:")
            for item in shopping_list:
              print(item)
            pass
        elif choice == 4:
            print(f"Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
