import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.name == other.name and self.email == other.email and
                    self.phone == other.phone and self.favorite == other.favorite)
        return False

    def __str__(self):
        favorite_status = "Yes" if self.favorite else "No"
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Favorite: {favorite_status}"


class AddressBook:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts

    def add_contact(self, contact: Person):
        self.contacts.append(contact)

    def remove_contact(self, contact: Person):
        self.contacts.remove(contact)

    def save_to_file(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return AddressBook(filename)

    def show_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook(filename)


def main():
    filename = "addressbook.pkl"
    address_book = load_data(filename)

    while True:
        command = input("Enter command (add/remove/show/exit): ").strip().lower()
        if command == "add":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            favorite = input("Is favorite (True/False): ").strip().lower() == "true"
            contact = Person(name, email, phone, favorite)
            address_book.add_contact(contact)
        elif command == "remove":
            name = input("Enter name of the contact to remove: ")
            contact_to_remove = next((c for c in address_book.contacts if c.name == name), None)
            if contact_to_remove:
                address_book.remove_contact(contact_to_remove)
            else:
                print("Contact not found")
        elif command == "show":
            address_book.show_contacts()
        elif command == "exit":
            break
        else:
            print("Invalid command")

    save_data(address_book, filename)


if __name__ == "__main__":
    main()
