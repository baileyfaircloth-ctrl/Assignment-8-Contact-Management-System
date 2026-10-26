
class Contact:
    '''
    Represents a contact with a name and phone number.
    '''

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    '''
    Represents one entry in the hash table.
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    Stores contacts using a hash table and linked lists.
    '''

    def __init__(self, size=10):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        current = self.data[index]

        # Update the number if the contact already exists
        while current:
            if current.key == key:
                current.value.number = number
                return
            current = current.next

        # Add a new contact to the beginning of the linked list
        contact = Contact(key, number)
        new_node = Node(key, contact)
        new_node.next = self.data[index]
        self.data[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for index, head in enumerate(self.data):
            print(f"Index {index}:", end=" ")

            current = head
            if current is None:
                print("Empty")
                continue

            while current:
                print(f"[{current.value}]", end=" -> ")
                current = current.next

            print("None")


# Test your hash table implementation
if __name__ == "__main__":
    table = HashTable(10)

    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")

    print("Initial hash table:")
    table.print_table()

    print("\nSearch for John:")
    print(table.search("John"))

    # Test collisions
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")

    print("\nHash table after adding Amy and May:")
    table.print_table()

    # Test updating an existing contact
    table.insert("Rebecca", "999-444-9999")
    print("\nRebecca after updating:")
    print(table.search("Rebecca"))

    # Test a contact that does not exist
    print("\nSearch for Chris:")
    print(table.search("Chris"))
