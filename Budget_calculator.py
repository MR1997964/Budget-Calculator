""""
Budgeting Tool Pseudo code:

Define a function to get a positive number from the user.
Continuously prompt the user until a valid positive number is entered.
If a negative number is entered, ask for a positive number.
If a non-numeric input is given, display an error message and ask again.
Return the valid positive number.

In the main function, display a welcome message.
Prompt the user for total income, total expenses, and desired savings amount.
Ensure all inputs are positive numbers.
Create an empty list for expense categories.

Begin a loop to collect categorized expenses:
Ask for an expense category or type "done" to finish.
If "done" is entered, exit the loop.
For each category entered, prompt for the expense amount.
Store the category and amount in the expense list.

Calculate the remaining budget by subtracting expenses and savings from income.
Display a message about the budget status:
If money is left, inform the user they can save money.
If the budget is zero, congratulate them on breaking even.
If over budget, suggest adjustments.

Provide a breakdown of expenses by category.
Ask the user if they want to save the summary to a CSV file.
If yes, save the categories and amounts to a CSV file.
Confirm the file has been saved successfully.

Define a function to save expenses to a CSV file:
Open a new CSV file for writing.
Write headers for categories and amounts.
Write each expense category and amount to the file.

Call the main function to start the program.
"""

import csv

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def export_to_csv(expenses_category):
    with open('expense_summary.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Amount'])  # Write headers
        for category, amount in expenses_category.items():
            writer.writerow([category, amount])  # Write each category and amount
    print("Expense summary saved to 'expense_summary.csv'.")

def main():
    print("Welcome to the Budgeting Tool.")
    total_income = get_float_input("Enter your total income: ")
    savings = get_float_input("Enter the amount of money you are willing to save: ")
    
    expenses_category = {}
    total_expenses = 0.0

    while True:
        category = input("Enter your expense category or type 'done' to finish: ").lower()
        if category == "done":
            break
        amount = get_float_input(f"Enter amount for {category}: ")
        expenses_category[category] = amount
        total_expenses += amount

    remaining_budget = total_income - total_expenses - savings
    if remaining_budget > 0:
        print("You can save money this month.")
    elif remaining_budget == 0:
        print("Congratulations! You are breaking even.")
    else:
        print("You are over budget. Please manage your expenses.")

    print("\nExpense Breakdown:")
    for category, amount in expenses_category.items():
        print(f"{category}: R{amount:.2f}")

    save_summary = input("Would you like to save this expense summary to a CSV file? (yes/no): ").lower()
    if save_summary == 'yes':
        export_to_csv(expenses_category)

# Start the program
main()

