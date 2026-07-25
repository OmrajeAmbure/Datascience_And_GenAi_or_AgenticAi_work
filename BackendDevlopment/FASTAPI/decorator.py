balance = 1000

def transaction_logger(func):
    def wrapper(*args, **kwargs):
        print("\n==========")
        print("Transaction Started")
        result = func(*args, **kwargs)
        print("Transaction Completed")
        print("==========")
        return result
    return wrapper

@transaction_logger
def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount}")


@transaction_logger
def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print(f"Withdraw ₹{amount}")


@transaction_logger
def check_balance():
    print(f"Current Balance: ₹{balance}")


deposit(500)
withdraw(200)
check_balance()