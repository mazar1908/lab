class Account:
    def __innit__(self,  name: str)-> str:
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        '''
        function to add money deposited into account
        :param amount: amount wanting to be deposited
        :return: account_balance + the amount deposited
        '''
        #self.amount: float = amount
        if amount <= 0:
            return False
        elif amount > 0:
            self.__account_balance = self.__account_balance + self.amount
            return True

    def withdraw (self, amount: float) -> bool:
        '''
        function to subtract the amount selected to be withdrawn from account_balance
        :param amount: amount wanting to be withdrew from account_balance
        :return: acount_balance - amount
        '''
        #self.amount = amount
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance = self.__account_balance - self.amount
            return True
    def get_balance(self) -> float:
        '''
        :return: return the final account balance associated with a name
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        :return: return the name associated with an account
        '''
        return self.__account_name
