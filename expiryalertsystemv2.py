
import json
from datetime import datetime, date
import os

FILE_NAME = "products.json"


def load_products():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_products(products):
    with open(FILE_NAME, "w") as file:
        json.dump(products, file, indent=4)


def add_product(products):
    name = input("Enter product name: ")
    expiry = input("Enter expiry date (DD-MM-YYYY): ")

    try:
        expiry_date = datetime.strptime(expiry, "%d-%m-%Y").date()

        products.append({
            "name": name,
            "expiry": expiry
        })

        save_products(products)
        print("Product added successfully!")

    except ValueError:
        print("Invalid date format!")


def view_products(products):
    today = date.today()

    if not products:
        print("No products saved yet.")
        return

    for product in products:
        expiry_date = datetime.strptime(
            product["expiry"], "%d-%m-%Y"
        ).date()

        days_left = (expiry_date - today).days

        if days_left < 0:
            status = "EXPIRED!"
        elif days_left <= 7:
            status = "EXPIRING SOON!"
        else:
            status = "SAFE FOR NOW"

        print(
            f'{product["name"]} | '
            f'{product["expiry"]} | '
            f'{days_left} days left | {status}'
        )


products = load_products()

while True:
    print("\n===== EXPIRY ALERT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product(products)
    elif choice == "2":
        view_products(products)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
