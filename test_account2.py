from pytest import *
from account2 import *
def setup_method(self):
        self.p1 = Account('Jerry')

    def test_init(self):
        assert self.p1.get_name() == Account("Jerry")
        assert self.p1.get_balance() == 0



    def test_deposit(self):
        assert self.p1.deposit(-15) is False
        assert self.p1.get_balance() == 0
        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == 0
        assert self.p1.deposit(15) is True
        assert self.p1.get_balance() == 15
        assert self.p1.deposit(1.2) is True

        assert self.p1.get_balance() == approx(16.2, abs=0.001)

    def test_deposit(self):
        assert self.p1.withdraw(-15) is False
        assert self.p1.get_balance() == 0
        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == 0

        self.p1.deposit(15)
        assert self.p1.withdraw(5) is True
        assert self.p1.get_balance() == 10
        assert self.p1.deposit(1.2) is True

        assert self.p1.get_balance() == approx(16.2, abs=0.001)



