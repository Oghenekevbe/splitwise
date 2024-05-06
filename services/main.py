from users import User
from expenses import Expense

def main():
    while True:
        command = input("Enter command: ").split()

        if command[0] == 'CREATE':
            if len(command) < 2:
                print("Invalid command. Please provide user ID.")
                continue
            user_id = command[1]
            username = input("Enter username: ")
            if not username:
                print("Invalid command. Please provide username.")
                continue
            email = input("Enter email: ")
            mobile_number = input("Enter mobile number: ")
            User(user_id=user_id, username=username, email=email, mobile_number=mobile_number)

        elif command[0] == 'EXPENSE':
            if len(command) < 5:
                print("Invalid command. Please provide all required arguments.")
                continue
            payer = command[1]
            amount = float(command[2])
            user_count = int(command[3])
            users = command[4:4+user_count]
            split_type = command[4+user_count]
            split_values = None
            if split_type == 'EXACT' or split_type == 'PERCENT':
                split_values = list(map(float, command[5+user_count:]))

            # Parse the users list into User objects
            users = [User.user_instances[user_id] for user_id in users]
            # Create and split the expense
            Expense(payer, amount, users, split_type, split_values).split_expense()

        elif command[0] == 'SHOW':
            if len(command) > 1:
                user_id = command[1]
                user = User.user_instances.get(user_id)
                if user:
                    if user.owes:
                        for owed_user_id, amount in user.owes.items():
                            owed_user = User.user_instances.get(owed_user_id)
                            if owed_user:
                                print(f"{user.username} owes {owed_user.username}: {amount}")
                    else:
                        print("No balance")
                else:
                    print("No user found with the provided ID.")
            else:
                any_balance = False
                for user in User.user_instances.values():
                    if user.owes:
                        any_balance = True
                        for owed_user_id, amount in user.owes.items():
                            owed_user = User.user_instances.get(owed_user_id)
                            if owed_user:
                                print(f"{user.username} owes {owed_user.username}: {amount}")
                if not any_balance:
                    print("No balance")
        elif command[0] == 'EXIT':
            break
        else:
            print("Invalid command. Please try again.")
if __name__ == "__main__":
    main()