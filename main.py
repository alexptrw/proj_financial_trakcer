transactions = []

def add_transactions():
    try:
        type = input('What is the type of the trancation(income/expense): ')
        if type not in ['income', 'expenses']:
            raise ValueError('Invalid Type. Please type (income/expense)')
            
    
        amount = float(input('What is the amount of the trancation:'))
        date = input('What is the date of the trancation:')
        description = input('What is the description of the trancation:')
        new_transaction = {
            type, 
            amount, 
            date, 
            description
        }
        transactions.append(new_transaction)

    except ValueError as e:
        print('Error:', e)

def view_transactions():
    for i in transactions:
        print(i)
    return transactions

def summary():
    total_income = 0
    total_expenses = 0

    for transaction in transactions:
        if transaction['type'] == 'income':
            total_income += transaction['amount']
        elif transaction['type'] == 'expense':
            total_expenses += transaction['amount']

    current_balance = total_income - total_expenses
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Current Balance: ${current_balance}")
    return current_balance

def main_menu():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_transactions()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            summary()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()