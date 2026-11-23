from plyer import notification
import json
from datetime import datetime, date
import os

FILE_NAME = "products.json"


def send_alert(product_name, days_left):
    if days_left == 3:
        message = f"{product_name} expires in 3 days!"
    elif days_left == 2:
        message = f"{product_name} expires in 2 days!"
    elif days_left == 1:
        message = f"{product_name} expires tomorrow!"
    else:
        message = f"{product_name} expires today!"

    # Terminal alert
    print("\n" + "!" * 45)
    print("EXPIRY ALERT:", message)
    print("!" * 45)

    # Desktop notification
    try:
        notification.notify(
              title="Expiry Alert System",
              message=message,
              app_name="Expiry Reminder",
              timeout=10
        )
    except Exception as error:
        print("Desktop notification failed:", error)

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
        if 0 <= days_left <= 3:
           send_alert(product["name"], days_left)

        if days_left < 0:
            status = "PRODUCT EXPIRED!"
        elif days_left == 0:
            status = "EXPIRES TODAY!"
        elif days_left == 1:
            status = "EXPIRES TOMORROW!"
        elif days_left <= 3:
            status = f"EXPIRING IN {days_left} DAYS!"
        else:
            status = "NO ALERT"

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
