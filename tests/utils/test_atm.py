from src.utils import ATM


def test_initial_balance() -> None:
    atm = ATM()
    assert atm.get_balance() == 0


def test_deposit() -> None:
    atm = ATM()
    result = atm.deposit(500)
    assert result == "500 deposited successfully"
    assert atm.get_balance() == 500


def test_multiple_deposits() -> None:
    atm = ATM()
    atm.deposit(200)
    atm.deposit(300)
    assert atm.get_balance() == 500


def test_withdraw() -> None:
    atm = ATM()
    atm.deposit(500)
    result = atm.withdraw(200)
    assert result == "200 withdrawn successfully"
    assert atm.get_balance() == 300


def test_withdraw_exact_balance() -> None:
    atm = ATM()
    atm.deposit(500)
    result = atm.withdraw(500)
    assert result == "500 withdrawn successfully"
    assert atm.get_balance() == 0


def test_withdraw_insufficient_balance() -> None:
    atm = ATM()
    atm.deposit(300)
    result = atm.withdraw(500)
    assert result == "Insufficient balance"
    assert atm.get_balance() == 300


def test_multiple_withdrawals() -> None:
    atm = ATM()
    atm.deposit(1000)
    atm.withdraw(300)
    atm.withdraw(200)
    assert atm.get_balance() == 500


def test_get_balance() -> None:
    atm = ATM()
    atm.deposit(750)
    assert atm.get_balance() == 750
