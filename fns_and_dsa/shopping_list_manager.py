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
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for add an item
            new_item = input('Add an item to the list: ')
            shopping_list.append(new_item)
            print(shopping_list)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input('enter an item to be removed from list: ')
            if remove_item not in shopping_list:
                print(remove_item, 'not found in the shoping list')
            else:
                shopping_list.remove(remove_item)
                print(shopping_list)
            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
