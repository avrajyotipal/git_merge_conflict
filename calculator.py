def calculate_discount(price):
    discount = price * 0.35
    return price - discount


price = 1000

final_price = calculate_discount(price)

print(f"Original Price: ₹{price}")
print(f"Final Price after discount: ₹{final_price}")