
from datetime import datetime, date

print("===== EXPIRY ALERT SYSTEM =====")

product = input("Enter product name: ")
expiry_input = input("Enter expiry date (DD-MM-YYYY): ")

expiry_date = datetime.strptime(
    expiry_input, "%d-%m-%Y"
).date()

today = date.today()
days_left = (expiry_date - today).days

if days_left < 0:
    print(product, "has expired!")
elif days_left <= 7:
    print(product, "is expiring soon!")
    print("Days remaining:", days_left)
else:
    print(product, "has not expired yet.")
    print("Days remaining:", days_left)
