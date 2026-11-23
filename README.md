# Expiry Alert System

A simple Python-based application that tracks product expiry dates and alerts users when products are expiring soon.

## Features
- Accepts product name and expiry date.
- Calculates the remaining days until expiry.
- Identifies already expired products.
- Displays an alert when a product is within 7 days of expiry.

## Technologies Used
- Python
- datetime module

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in your terminal.
4. Run:

```bash
python expiry_alert.py
```

## Input Format

Enter the expiry date in `DD-MM-YYYY` format.

Example: `26-11-2026`

## Future Improvements
- Barcode scanning for product identification.
- Automatic product information retrieval.
- Product inventory management.
- Expiry reminders starting 3 days before expiry.
- OCR-based expiry date detection.

## Note
This is an initial version of the project. It provides expiry reminders and does not determine product safety.
