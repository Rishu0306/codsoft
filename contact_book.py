def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    print()  # Add an empty line for better readability

def add_contact(contacts):
    name = input("Enter the contact name: ")
    phone = input("Enter the contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added successfully.\n")

def search_contact(contacts):
    name = input("Enter the contact name to search: ")
    phone = contacts.get(name, "Contact not found.")
    print(f"{name}: {phone}\n")

def main():
    contacts = {}
    
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
