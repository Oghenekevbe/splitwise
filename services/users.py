user_instances = {}
class User:
    def __init__(self, user_id, name, email, mobile_number):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.balance = 0  # Initialize balance to zero
        # Store the instance in the global dictionary
        user_instances[user_id] = self
