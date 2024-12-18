import tkinter as tk
from tkinter import messagebox

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

class PortableToiletRentalApp:
    def __init__(self, root):
        self.rental_system = PortableToiletRental()
        self.root = root
        self.root.title("Portable Toilet Rental System")

        # Add Toilet Section
        tk.Label(root, text="Toilet ID:").grid(row=0, column=0, padx=10, pady=5)
        self.toilet_id_entry = tk.Entry(root)
        self.toilet_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(root, text="Add Toilet", command=self.add_toilet).grid(row=0, column=2, padx=10, pady=5)

        # Rent Toilet Section
        tk.Label(root, text="Customer Name:").grid(row=1, column=0, padx=10, pady=5)
        self.customer_name_entry = tk.Entry(root)
        self.customer_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(root, text="Rent Toilet", command=self.rent_toilet).grid(row=1, column=2, padx=10, pady=5)

        # Return Toilet Section
        tk.Button(root, text="Return Toilet", command=self.return_toilet).grid(row=2, column=2, padx=10, pady=5)

        # Delete Toilet Section
        tk.Button(root, text="Delete Toilet", command=self.delete_toilet).grid(row=3, column=2, padx=10, pady=5)

        # View Inventory Section
        tk.Button(root, text="View Inventory", command=self.view_inventory).grid(row=4, column=2, padx=10, pady=5)

        # Output Section
        self.output_text = tk.Text(root, width=50, height=10, state=tk.DISABLED)
        self.output_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    def display_message(self, message):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.config(state=tk.DISABLED)

    def add_toilet(self):
        toilet_id = self.toilet_id_entry.get().strip()
        if toilet_id:
            message = self.rental_system.add_toilet(toilet_id)
            self.display_message(message)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid Toilet ID.")

    def rent_toilet(self):
        toilet_id = self.toilet_id_entry.get().strip()
        customer_name = self.customer_name_entry.get().strip()
        if toilet_id and customer_name:
            message = self.rental_system.rent_toilet(toilet_id, customer_name)
            self.display_message(message)
        else:
            messagebox.showwarning("Input Error", "Please enter both Toilet ID and Customer Name.")

    def return_toilet(self):
        toilet_id = self.toilet_id_entry.get().strip()
        if toilet_id:
            message = self.rental_system.return_toilet(toilet_id)
            self.display_message(message)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid Toilet ID.")

    def delete_toilet(self):
        toilet_id = self.toilet_id_entry.get().strip()
        if toilet_id:
            message = self.rental_system.delete_toilet(toilet_id)
            self.display_message(message)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid Toilet ID.")

    def view_inventory(self):
        message = self.rental_system.view_inventory()
        self.display_message(message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PortableToiletRentalApp(root)
    root.mainloop()
