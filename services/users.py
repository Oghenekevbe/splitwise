# user_instances = {}
# class User:
#     def __init__(self, user_id, name, email, mobile_number):
#         self.user_id = user_id
#         self.name = name
#         self.email = email
#         self.mobile_number = mobile_number
#         self.balance = 0  # Initialize balance to zero
#         # Store the instance in the global dictionary
#         user_instances[user_id] = self

user_instances = {}

class User:
    def __init__(self, user_id, username, email, mobile_number):
        self.username = username
        self.balance = 0 
        self.email = email 
        self.user_id = user_id
        self.mobile_number = mobile_number
        user_instances[user_id] = self

    def __str__(self):
        return f"Username: {self.username}, Balance: {self.balance}, Email: {self.email}, Mobile: {self.mobile_number} "

def create_user():
    user_id = input("Enter user ID: ")
    username = input("Enter username: ")
    email = input("Enter email (optional): ") or None
    mobile_number = input("Enter mobile number: ")
    new_user = User(user_id, username, email, mobile_number)
    return new_user

new_use = create_user()
print("User created successfully!")
print(new_use)
