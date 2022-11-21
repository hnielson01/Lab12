import pytest
from account import *

def test_init():
    acc1 = account("Bob")
    assert acc1.getname() == "Bob"
    assert acc1.getBalance() == 0

def test_deposit():
    acc1 = account("Bob")
    acc1.deposit(20)
    assert acc1.getBalance() == 20

def test_withdraw():
    acc1 = account("Bob")
    acc1.deposit(100)
    acc1.withdraw(20)
    assert acc1.getBalance() == 80