class Account:
    def __innit__(self,  name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount <= 0:
            return False
        elif amount > 0:
            self.account_balance = account_balance + amount
            return True

    def withdraw (self, amount):
        if amount <= 0 or amount > account_balance:
            return False
        else:
            account_balance = account_balance - amount
            return True
    def get_balance(self):
        return account_balance

    def get_name(self):
        return amount
