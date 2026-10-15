
# Contact Management System Using Hash Tables
# Collision Resolution: Separate Chaining

SIZE = 10
hash_table = [[] for _ in range(SIZE)]


# Hash Function
def hash_function(name):
    return sum(ord(ch.lower()) for ch in name) % SIZE


# Add Contact
def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty!")
        return

    if not phone.isdigit() or len(phone) != 10:
        print("Enter a valid 10-digit phone number!")
        return

    index = hash_function(name)

    # Check if contact already exists
    for contact in hash_table[index]:
        if contact[0].lower() == name.lower():
            contact[1] = phone
            print("Contact updated successfully!")
            return

    hash_table[index].append([name, phone])
    print("Contact added successfully!")
    print("Hash Index:", index)


# Search Contact
def search_contact():
    name = input("Enter name to search: ").strip()
    index = hash_function(name)

    for contact in hash_table[index]:
        if contact[0].lower() == name.lower():
            print("\nContact Found!")
            print("Name:", contact[0])
            print("Phone:", contact[1])
            print("Hash Index:", index)
            return

    print("Contact not found!")


# Update Contact
def update_contact():
    name = input("Enter name to update: ").strip()
    index = hash_function(name)

    for contact in hash_table[index]:
        if contact[0].lower() == name.lower():
            phone = input("Enter new phone number: ").strip()

            if not phone.isdigit() or len(phone) != 10:
                print("Enter a valid 10-digit phone number!")
                return

            contact[1] = phone
            print("Contact updated successfully!")
            return

    print("Contact not found!")


# Delete Contact
def delete_contact():
    name = input("Enter name to delete: ").strip()
    index = hash_function(name)

    for contact in hash_table[index]:
        if contact[0].lower() == name.lower():
            hash_table[index].remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found!")


# Display All Contacts
def display_contacts():
    found = False
    print("\n----- All Contacts -----")

    for index, bucket in enumerate(hash_table):
        for contact in bucket:
            print("Name:", contact[0],
                  "| Phone:", contact[1],
                  "| Hash Index:", index)
            found = True

    if not found:
        print("No contacts available.")


# Display Hash Table
def display_hash_table():
    print("\n----- Hash Table -----")

    for index, bucket in enumerate(hash_table):
        print(index, ":", bucket)


# Main Menu
def main():
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Display Hash Table")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            search_contact()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            display_contacts()

        elif choice == "6":
            display_hash_table()

        elif choice == "7":
            print("Thank you for using Contact Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the application
if __name__ == "__main__":
    main()
