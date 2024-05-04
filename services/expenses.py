# Assuming a global dictionary to store User instances
user_instances = {}

ExpenseManager = {}

class User:
    def __init__(self, user_id, name, email, mobile_number):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.balance = 0  # Initialize balance to zero
        # Store the instance in the global dictionary
        user_instances[user_id] = self

class Expense:
    def __init__(self, paid_by: User, amount, user_count ,splits,percentages,split_type):

        self.paid_by = paid_by
        self.amount = amount
        self.user_count = user_count
        self.splits = splits  # the list of people you're splitting by
        self.percentages = percentages
        self.split_type = split_type




    def split_expense(self):
        paid_by = self.paid_by.user_id
        splits = [user.user_id for user in self.splits]
        percentages = self.percentages

        if self.split_type == "EQUAL":
            self.percentages = None
            split_amount = round(self.amount / (len(splits)), 2)
            for user_id in splits:
                if user_id != paid_by:
                    # Get the current balance of users before the transaction
                    paid_by_user = user_instances[paid_by]
                    paid_by_balance_before = paid_by_user.balance
                    
                    user = user_instances[user_id]
                    user_balance_before = user.balance

                    # Update the balances
                    paid_by_user.balance -= split_amount
                    user.balance += split_amount

                    # Get the current balance of users after the transaction
                    paid_by_balance_after = paid_by_user.balance
                    user_balance_after = user.balance

                    # Append the string to the list with the updated balance
                    if paid_by not in ExpenseManager:
                        ExpenseManager[paid_by] = []
                    ExpenseManager[paid_by].append(
                        f"{user_id} owes {paid_by}: {user_balance_after} ({user_balance_before}+{split_amount})"
                    )

        elif self.split_type == "EXACT":
            if len(splits) != len(percentages):
                raise ValueError("Number of splits must match number of exact amounts")
            if sum(percentages) != self.amount:
                raise ValueError("Sum of exact amounts must be equal to total amount")
                
            for i, user_id in enumerate(splits):
                if user_id != paid_by:
                    split_amount = percentages[i]
                    # Get the current balance of users before the transaction
                    paid_by_user = user_instances[paid_by]
                    paid_by_balance_before = paid_by_user.balance
                    
                    user = user_instances[user_id]
                    user_balance_before = user.balance

                    # Update the balances
                    paid_by_user.balance -= split_amount
                    user.balance += split_amount

                    # Get the current balance of users after the transaction
                    paid_by_balance_after = paid_by_user.balance
                    user_balance_after = user.balance

                    # Append the string to the list with the updated balance
                    if paid_by not in ExpenseManager:
                        ExpenseManager[paid_by] = []
                    ExpenseManager[paid_by].append(
                        f"{user_id} owes {paid_by}: {split_amount} (0+{split_amount})"
                    )

        elif self.split_type == "PERCENT":
            if percentages is None:
                raise ValueError("Percentages must be provided for 'PERCENT' split type")
            if len(percentages) != self.user_count:
                raise ValueError("Number of percentages must match number of splits")
            if sum(percentages) != 100:
                raise ValueError("Percentages must sum up to 100")
            
            for i, user_id in enumerate(splits):
                if user_id != paid_by:
                    split_amount = round(self.amount * (percentages[i] / 100), 2)
                    # Get the current balance of users before the transaction
                    paid_by_user = user_instances[paid_by]
                    paid_by_balance_before = paid_by_user.balance
                    
                    user = user_instances[user_id]
                    user_balance_before = user.balance

                    # Update the balances
                    paid_by_user.balance -= split_amount
                    user.balance += split_amount

                    # Get the current balance of users after the transaction
                    paid_by_balance_after = paid_by_user.balance
                    user_balance_after = user.balance

                    # Append the string to the list with the updated balance
                    if paid_by not in ExpenseManager:
                        ExpenseManager[paid_by] = []
                    ExpenseManager[paid_by].append(
                        f"{user_id} owes {paid_by}: {split_amount} (0+{split_amount})"
                    )

        latest_expense = ExpenseManager[paid_by][-(len(splits) - 1) :]
        # Convert the list to a string
        latest_expense_str = "\n".join(latest_expense)
        print(latest_expense_str)
        return latest_expense_str
