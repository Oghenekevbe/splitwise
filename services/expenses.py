from users import User


class Expense:
    def __init__(self, paid_by, amount, users, split_type, split_values=None):
        self.paid_by = paid_by
        self.amount = amount
        self.users = users
        self.split_type = split_type
        self.split_values = split_values

    def split_expense(self):
        if self.split_type == 'EQUAL':
            split_amount = self.amount / len(self.users)
            for user in self.users:
                if user.user_id != self.paid_by:
                    self._update_balances(self.paid_by, user.user_id, split_amount)
        elif self.split_type == 'EXACT':
            for i, user in enumerate(self.users):
                if user.user_id != self.paid_by:
                    self._update_balances(self.paid_by, user.user_id, self.split_values[i])
        elif self.split_type == 'PERCENT':
            for i, user in enumerate(self.users):
                if user.user_id != self.paid_by:
                    split_amount = self.amount * (self.split_values[i] / 100)
                    self._update_balances(self.paid_by, user.user_id, split_amount)

    def _update_balances(self, paid_by, user_id, split_amount):
        paid_by_user = User.user_instances[paid_by]
        user = User.user_instances[user_id]

        # Check if user already owes paid_by_user
        if user_id in paid_by_user.owes:
            owed_amount = paid_by_user.owes[user_id]
            if owed_amount > split_amount:
                paid_by_user.owes[user_id] -= split_amount
                user.is_owed[paid_by] -= split_amount
            else:
                del paid_by_user.owes[user_id]
                del user.is_owed[paid_by]
                paid_by_user.is_owed[user_id] = split_amount - owed_amount
                user.owes[paid_by] = split_amount - owed_amount
        # Check if paid_by_user already owes user
        elif paid_by in user.owes:
            owed_amount = user.owes[paid_by]
            if owed_amount > split_amount:
                user.owes[paid_by] -= split_amount
                paid_by_user.is_owed[user_id] -= split_amount
            else:
                del user.owes[paid_by]
                del paid_by_user.is_owed[user_id]
                user.is_owed[paid_by] = split_amount - owed_amount
                paid_by_user.owes[user_id] = split_amount - owed_amount
        # If neither user owes the other, then simply update the balances
        else:
            paid_by_user.is_owed[user_id] = split_amount
            user.owes[paid_by] = split_amount