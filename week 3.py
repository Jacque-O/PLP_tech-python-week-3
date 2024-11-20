def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if the discount is 20% or higher."""
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount_percent)
    if discount_percent >= 20:
        print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")
