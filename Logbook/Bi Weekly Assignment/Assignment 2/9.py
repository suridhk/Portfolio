'''
9.Write a function named update_weekly_sales that takes a dictionary of weekly sales data, a day name, and a sale amount.
If the day already exists, update the sale amount by adding the new amount.
If the day does not exist, add it to the dictionary.
Return the updated dictionary.
'''

def update_weekly_sales(sales_data, day, amount):
    """
    Updates the sales dictionary with a new amount for a specific day.
    """
    # Use .get() or a simple if/else to check for the day's existence
    if day in sales_data:
        sales_data[day] += amount
    else:
        sales_data[day] = amount
        
    return sales_data

# Example Usage:
weekly_sales = {"Monday": 150, "Tuesday": 200}

# Updating an existing day
update_weekly_sales(weekly_sales, "Monday", 50)

# Adding a new day
update_weekly_sales(weekly_sales, "Wednesday", 100)

print(weekly_sales)
# Output: {'Monday': 200, 'Tuesday': 200, 'Wednesday': 100}