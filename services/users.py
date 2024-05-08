
class User:
    user_instances = {}

    def __init__(self, user_id, username, email, mobile_number):
        self.username = username
        self.balance = 0 
        self.email = email 
        self.user_id = user_id
        self.mobile_number = mobile_number
        User.user_instances[user_id] = self
        self.debtors = {}  # Tracks who owes this user
        self.creditors = {}  # Tracks who this user owes

    def add_owed(self, user_id, amount):
        try:
            if user_id in self.creditors:
                self.creditors[user_id] -= amount
                if self.creditors[user_id] <= 0:
                    del self.creditors[user_id]
            else:
                self.creditors[user_id] = amount
        except Exception as e:
            print(f"an error occured: {e}")

    def add_is_owed(self, user_id, amount):
        try:
            if user_id in self.debtors:
                self.debtors[user_id] -= amount
                if self.debtors[user_id] <= 0:
                    del self.debtors[user_id]
            else:
                self.debtors[user_id] = amount
        except Exception as e:
            print(f"an error occured: {e}")
