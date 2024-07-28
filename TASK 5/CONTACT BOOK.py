import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    """View the list of all contacts."""
    if not contacts:
        print("No contacts available.")
        return
    print(f"{'Name':<20} {'Phone':<15}")
    print("-" * 35)
    for name, info in contacts.items():
        print(f"{name:<20} {info['phone']:<15}")

def search_contact(contacts):
    """Search for a contact by name or phone number."""
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info['phone']:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("-" * 30)
            found = True
    if not found:
        print("No contact found.")

def update_contact(contacts):
    """Update contact details."""
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return
    print("Enter new details (leave blank to keep current value):")
    phone = input(f"Phone ({contacts[name]['phone']}): ") or contacts[name]['phone']
    email = input(f"Email ({contacts[name]['email']}): ") or contacts[name]['email']
    address = input(f"Address ({contacts[name]['address']}): ") or contacts[name]['address']
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print("Contact updated successfully.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
