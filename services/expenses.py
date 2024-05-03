
UserManager = {}

class User:

    def __init__(self, user_id, name, email, mobile_number):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.balance = {}  # Dictionary to store balances with other users


    


ExpenseManager = {}


class Expense:
    def __init__(self, paid_by: User, amount, split_type,percentages,splits):

        self.paid_by = paid_by
        self.amount = amount
        self.split_type = split_type
        self.splits = splits  # the list of people you're splitting by
        self.percentages = percentages


    def split_expense(self):
        paid_by = self.paid_by.user_id
        splits = [user.user_id for user in self.splits]
        percentages = self.percentages

        if self.split_type == "EQUAL":
            split_amount = round(self.amount / (len(splits)), 2)
            for user_id in splits:
                if user_id != paid_by:
                    # Create the key with an empty list if it doesn't exist
                    if paid_by not in ExpenseManager:
                        ExpenseManager[paid_by] = []

                    # Append the string to the list
                    ExpenseManager[paid_by].append(
                        f"{user_id} owes {paid_by}: {split_amount} (0+{split_amount})"
                    )
                    # return only the latest transactions entered into the expense manager
            latest_expense = ExpenseManager[paid_by][-(len(splits) - 1) :]
            # Convert the list to a string
            latest_expense_str = "\n".join(latest_expense)
            print(latest_expense_str)
            return latest_expense_str

        elif self.split_type == "EXACT":
            if len(splits) != len(percentages):
                raise ValueError("Number of splits must match number of exact amounts")
            if sum(percentages) != self.amount:
                raise ValueError("sum of exact amounts must be equal to total amount")
                
            for i, user_id in enumerate(splits):
                if user_id != paid_by:
                    split_amount = percentages[i]
                    # Create the key with an empty list if it doesn't exist
                    if paid_by not in ExpenseManager:
                        ExpenseManager[paid_by] = []

                    # Append the string to the list
                    ExpenseManager[paid_by].append(
                        f"{user_id} owes {paid_by}: {split_amount} (0+{split_amount})"
                    )

            latest_expense = ExpenseManager[paid_by][-(len(splits) - 1) :]
            # Convert the list to a string
            latest_expense_str = "\n".join(latest_expense)

            print(latest_expense_str)
            return latest_expense_str




        elif self.split_type == "PERCENT":
            if percentages is None:
                raise ValueError("Percentages must be provided for 'PERCENTAGE' split type")
            if len(percentages) != len(self.splits):
                raise ValueError("Number of percentages must match number of splits")
            if sum(percentages) != 100:
                raise ValueError("Percentages must sum up to 100")
            
        for i,user_id in enumerate(splits):
            if user_id != paid_by:
                split_amount = round(self.amount*(percentages[i]/100),2)

                # Create the key with an empty list if it doesn't exist
                if paid_by not in ExpenseManager:
                    ExpenseManager[paid_by] = []
                # Append the string to the list
                ExpenseManager[paid_by].append(
                        f"{user_id} owes {paid_by}: {split_amount} (0+{split_amount})"
                    )
        latest_expense = ExpenseManager[paid_by][-(len(splits) - 1) :]
        # Convert the list to a string
        latest_expense_str = "\n".join(latest_expense)
        print(latest_expense_str)
        return latest_expense_str

            
