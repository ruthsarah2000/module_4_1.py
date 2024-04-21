import contacts_manager

def main():
    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the contact: ")
            phone_number = input("Enter the phone number of the contact: ")
            contacts_manager.add_contact(name, phone_number)
        elif choice == "2":
            name = input("Enter the name of the contact to remove: ")
            contacts_manager.remove_contact(name)
        elif choice == "3":
            contacts_manager.display_contacts()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
