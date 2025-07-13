from typing import Dict


print("🧾 Welcome to LifeCare Medical Store")
print("Available Medicines:")
print("1. Paracetamol     - ₹30")
print("2. Cough Syrup     - ₹75")
print("3. Antibiotic Tabs - ₹120")
print("4. Pain Relief Gel - ₹90")
print("5. Vitamin D       - ₹50")

# Function to calculate GST
def calculate_medicine(subtotal: float) -> float:
    return round(subtotal * 0.12, 2)  # 12% GST (as per your output)

# Function to display final bill
def display_medicine(items: Dict[str, float]) -> None:
    print("\n💊 Final Bill:")
    print("Medicine         Price")
    print("------------------------")

    for idx, (item, price) in enumerate(items.items(), start=1):
        print(f"{item:<16} ₹{price}")

    subtotal = sum(items.values())
    gst = calculate_medicine(subtotal)
    total = subtotal + gst

    print("\n------------------------")
    print(f"Subtotal:         ₹{subtotal:.2f}")
    print(f"GST (12%):        ₹{gst:.2f}")
    print(f"Total Amount:     ₹{total:.2f}")
    print("------------------------")
    print("\n🧡 Thank you! Get well soon.")

# Function to collect medicine and price
def get_items() -> Dict[str, float]:
    items = {}
    while (item := input("Enter medicine name (or press Enter to finish): ")) != "":
        try:
            price = float(input(f"Enter price for {item}: ₹"))
        except ValueError:
            print("❌ Invalid price. Please enter a number.")
        else:
            items[item] = price
        finally:
            print("---")
    return items

# Main program
if __name__ == "__main__":
    items = get_items()
    if items:
        display_medicine(items)
    else:
        print("No medicines entered. Bill not generated.")
