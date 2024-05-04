import unittest
from services.users import User, user_instances
from services.expenses import Expense, ExpenseManager

class TestExpense(unittest.TestCase):
    def setUp(self):
        # Creating users for testing
        self.user1 = User(user_id=1, name="User 1", email="user1@example.com", mobile_number="1234567890")
        self.user2 = User(user_id=2, name="User 2", email="user2@example.com", mobile_number="9876543210")
        self.user3 = User(user_id=3, name="User 3", email="user3@example.com", mobile_number="5555555555")
        self.user4 = User(user_id=4, name="User 4", email="user4@example.com", mobile_number="9999999999")
        
    def test_equal_split(self):
        # Test equal split type
        expense = Expense(paid_by=self.user1, amount=100, user_count=3, splits=[self.user2, self.user3], percentages=None, split_type="EQUAL")
        expense.split_expense()
        # Check balances
        self.assertEqual(self.user1.balance, 0)
        self.assertEqual(self.user2.balance, 50)
        self.assertEqual(self.user3.balance, 50)
        # Check ExpenseManager
        self.assertEqual(len(ExpenseManager[self.user1.user_id]), 2)  # Assuming two users were split
        
    def test_exact_split(self):
        # Test exact split type
        expense = Expense(paid_by=self.user1, amount=100, user_count=3, splits=[self.user2, self.user3], percentages=[30, 70], split_type="EXACT")
        expense.split_expense()
        # Check balances
        self.assertEqual(self.user1.balance, 0)
        self.assertEqual(self.user2.balance, 30)
        self.assertEqual(self.user3.balance, 70)
        # Check ExpenseManager
        self.assertEqual(len(ExpenseManager[self.user1.user_id]), 2)  # Assuming two users were split
        
    def test_percent_split(self):
        # Test percent split type
        expense = Expense(paid_by=self.user1, amount=100, user_count=3, splits=[self.user2, self.user3], percentages=[25, 75], split_type="PERCENT")
        expense.split_expense()
        # Check balances
        self.assertEqual(self.user1.balance, 0)
        self.assertEqual(self.user2.balance, 25)
        self.assertEqual(self.user3.balance, 75)
        # Check ExpenseManager
        self.assertEqual(len(ExpenseManager[self.user1.user_id]), 2)  # Assuming two users were split

if __name__ == '__main__':
    unittest.main()
