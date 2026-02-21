contacts = {}

while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contacts[name] = [phone, email, address]
        print("Contact added.")

    elif choice == "2":
        for name, details in contacts.items():
            print(name, ":", details[0])

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print("Details:", contacts[search])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contacts:
            contacts[name][0] = input("New Phone: ")
            contacts[name][1] = input("New Email: ")
            contacts[name][2] = input("New Address: ")
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice.")
