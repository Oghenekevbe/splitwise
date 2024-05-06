
class User:
    user_instances = {}

    def __init__(self, user_id, username, email, mobile_number):
        self.username = username
        self.balance = 0 
        self.email = email 
        self.user_id = user_id
        self.mobile_number = mobile_number
        User.user_instances[user_id] = self
        self.owes = {}  # Tracks who owes this user
        self.is_owed = {}  # Tracks who this user owes

    def add_owed(self, user_id, amount):
        if user_id in self.is_owed:
            self.is_owed[user_id] -= amount
            if self.is_owed[user_id] <= 0:
                del self.is_owed[user_id]
        else:
            self.is_owed[user_id] = amount

    def add_is_owed(self, user_id, amount):
        if user_id in self.owes:
            self.owes[user_id] -= amount
            if self.owes[user_id] <= 0:
                del self.owes[user_id]
        else:
            self.owes[user_id] = amount
