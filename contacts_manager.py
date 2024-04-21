contacts = []

def add_contact(name, phone_number):
    
    contacts.append({"name": name, "phone_number": phone_number})
    print(f"Contact {name} added successfully.")

def remove_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"Contact {name} removed successfully.")
            return
    print(f"Contact {name} not found in the contact list.")

def display_contacts():
    
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}")
