# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Example of expected output line (do not remove):
def calculate_revenue(prices, quantities_sold):
    # Initialize a list to store the calculated revenues
    revenue = []
    # Multiply each price by its corresponding quantity sold
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

def formatted_output(revenues):
    for product, rev in sorted(revenues):
        print(f"{product} has total revenue of ${rev}")

# Calculate revenue list
revenue = calculate_revenue(prices, quantities_sold)

# Combine products with their revenues
revenue_per_product = list(zip(products, revenue))

# Display formatted output
formatted_output(revenue_per_product)