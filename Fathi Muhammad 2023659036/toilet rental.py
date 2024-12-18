class PortableToiletRental:
    def __init__(self):
        self.inventory = {}
        self.rented = {}

    def add_toilet(self, toilet_id):
        if toilet_id in self.inventory or toilet_id in self.rented:
            return f"Toilet ID {toilet_id} already exists."
        else:
            self.inventory[toilet_id] = "Available"
            return f"Toilet ID {toilet_id} added to inventory."

    def rent_toilet(self, toilet_id, customer_name):
        if toilet_id in self.inventory and self.inventory[toilet_id] == "Available":
            self.inventory[toilet_id] = "Rented"
            self.rented[toilet_id] = customer_name
            return f"Toilet ID {toilet_id} rented to {customer_name}."
        elif toilet_id in self.rented:
            return f"Toilet ID {toilet_id} is already rented by {self.rented[toilet_id]}."
        else:
            return f"Toilet ID {toilet_id} does not exist in inventory."

    def return_toilet(self, toilet_id):
        if toilet_id in self.rented:
            customer_name = self.rented.pop(toilet_id)
            self.inventory[toilet_id] = "Available"
            return f"Toilet ID {toilet_id} returned by {customer_name}."
        else:
            return f"Toilet ID {toilet_id} is not currently rented."

    def delete_toilet(self, toilet_id):
        if toilet_id in self.inventory:
            if toilet_id in self.rented:
                self.rented.pop(toilet_id)
            self.inventory.pop(toilet_id)
            return f"Toilet ID {toilet_id} has been deleted from the system."
        else:
            return f"Toilet ID {toilet_id} does not exist in the system."

    def view_inventory(self):
        inventory_status = "\nCurrent Inventory Status:\n"
        for toilet_id, status in self.inventory.items():
            customer = self.rented.get(toilet_id, "N/A")
            inventory_status += f"ID: {toilet_id}, Status: {status}, Rented by: {customer if status == 'Rented' else 'N/A'}\n"
        return inventory_status

def main():
    rental_system = PortableToiletRental()
    while True:
        print("\n--- Portable Toilet Rental System ---")
        print("1. Add Toilet")
        print("2. Rent Toilet")
        print("3. Return Toilet")
        print("4. Delete Toilet")
        print("5. View Inventory")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            toilet_id = input("Enter Toilet ID to add: ").strip()
            if toilet_id:
                print(rental_system.add_toilet(toilet_id))
            else:
                print("Invalid input. Please provide a valid Toilet ID.")

        elif choice == "2":
            toilet_id = input("Enter Toilet ID to rent: ").strip()
            customer_name = input("Enter Customer Name: ").strip()
            if toilet_id and customer_name:
                print(rental_system.rent_toilet(toilet_id, customer_name))
            else:
                print("Invalid input. Please provide both Toilet ID and Customer Name.")

        elif choice == "3":
            toilet_id = input("Enter Toilet ID to return: ").strip()
            if toilet_id:
                print(rental_system.return_toilet(toilet_id))
            else:
                print("Invalid input. Please provide a valid Toilet ID.")

        elif choice == "4":
            toilet_id = input("Enter Toilet ID to delete: ").strip()
            if toilet_id:
                print(rental_system.delete_toilet(toilet_id))
            else:
                print("Invalid input. Please provide a valid Toilet ID.")

        elif choice == "5":
            print(rental_system.view_inventory())

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
