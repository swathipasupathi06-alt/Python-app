# Simple Contact Manager Application

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"{name} added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\nSaved Contacts:")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")
        print()

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully!\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("===== Contact Manager =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice\n")

menu()