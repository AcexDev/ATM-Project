import time
import sys
import random
from datetime import datetime
from User_ops import profile
def display_header():
    print("=" * 30)
    print("ACEX_DEV ATM MACHINE ©️".center(30))
    print("=" * 30)
    print()


def display_main_menu():
    print(f"""
{"="*30}
HELLO THERE! WELCOME 😄
{"-"*30}
DASHBOARD
1 - 📰 View Balance
2 - 💸 Withdrawals
3 - 💰 Deposits
4 - 📤 Transfers
5 - 👤 User
6 - 🚪 Exit
{"="*30}
""")

def post_action():
    print("""
OPTIONS:
1 - Return to dashboard
Any other key to remain
""")

def initialize_atm():
    display_header()
    print("To start, enter '1' (any other key to exit)")
    begin = input("> ")
    if begin != "1":
        sys.exit("Program exited. You chose not to continue.\nPlease run the program again and choose '1' to continue")


def login_sequence(acct_pin="1234"):
    print(f"""
{"-"*30}
Welcome to Acex ATM services
Navigating your experience:
{"-"*30}\n""")

    print("Please Insert a valid card 💳")
    print("\nIs card Inserted?\n- YES: Enter '1'\n- NO: Enter '2'")
    present = input("> ")
    if present == "1":
        attempts = 3
        while attempts > 0:
            try:
                pin = int(input("Enter account PIN(4 digits): "))
                pin = str(pin)

                if len(pin) != 4:
                    print("Account PIN should be exactly 4 digits.\n")
                elif pin == acct_pin:
                    print("Login Successful!\n")
                    print("Access Granted.🔓\nProceeding to Dashboard.🔃 Please Wait...")
                    time.sleep(1)
                    break
                else:
                    attempts -= 1
                    if attempts == 0:
                        sys.exit("\nPIN limit reached – Account restricted.\nVisit any of our offices for further actions.")
                    else:
                        print(f"Invalid PIN. You have {attempts} attempt(s) left!\n")
            except ValueError:
                print("Invalid input! PIN must contain only numbers.\n")
    else:
        print("Card not detected. Try again!")
        sys.exit()


def check_balance(balance):
    while True:
        print("=" * 30)
        print(f"CURRENT BALANCE: #{balance:,.2f}".center(30))
        print("=" * 30)
        post_action()
        action = input("> ")
        if action == "1":
            break
        else:
            continue



def handle_withdrawal(balance, trans_pin):
    while True:
        try:
            amount = float(input("Amount to withdraw - #"))
            time.sleep(0.5)
            if amount > balance:
                print("Insufficient funds. Please try a smaller amount.")
            elif amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                user_trans_pin = input("Enter transaction pin: ")
                print("Processing Transaction. Please Wait.")
                time.sleep(1.5)
                if user_trans_pin != trans_pin:
                    print("Invalid Pin. Transaction cancelled.")
                else:
                    balance -= amount
                    ref = "TXN" + str(random.randint(10000000, 99999999))
                    timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
                    print(f"""
                    {"=" * 40}
                    {"**TRANSACTION RECEIPT**".center(40)}
                    {"=" * 40}
                    Date & time      : {timestamp}
                    Reference No.    : {ref}
                    Amount withdrawn : #{amount:,.2f}
                    New balance      : #{balance:,.2f}
                    {"-" * 40}
                    {"Thanks for banking with us!".center(40)}
                    {"Powered by Acex_Dev Team ©️".center(40)}
                    {"=" * 40}
                    """)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        post_action()
        action = input("> ")
        if action == "1":
            break
        else:
            continue
    return balance



def handle_deposit(balance, trans_pin):
    while True:
        try:
            dep_amount = float(input("Amount to deposit - #"))
            time.sleep(1)
            if dep_amount < 10:
                print("Minimum deposit is #10")
            elif dep_amount > 200000:
                print("Maximum deposit is #200,000")
            else:
                time.sleep(0.5)
                print("Processing Transaction. Please Wait.")
                time.sleep(1.5)
                balance += dep_amount
                ref = "TXN" + str(random.randint(10000000, 99999999))
                timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
                print(f"""
                {"=" * 40}
                {"**TRANSACTION RECEIPT**".center(40)}
                {"=" * 40}
                Date & time      : {timestamp}
                Reference No.    : {ref}
                Amount deposited : #{dep_amount:,.2f}
                New balance      : #{balance:,.2f}
                {"-" * 40}
                {"Thanks for banking with us!".center(40)}
                {"Powered by Acex_Dev Team ©️".center(40)}
                {"=" * 40}
                """)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        post_action()
        action = input("> ")
        if action == "1":
            break
        else:
            continue
    return balance



def avail_banks():
    print(f"""
Choose Bank:
1. Opay
2. Palmpay
3. Moniepoint
4. Acex Bank
5. Zenith
6. First Bank
7. GT Bank
""")

def transfer(balance, trans_pin):
    while True:
        recipient_acct_no = input("Enter recipient account number(10 digits): ")
        if len(recipient_acct_no) != 10 or not recipient_acct_no.isdigit():
            print("Invalid! Account numbers should be 10 digits.")
        else:
            avail_banks()
            bank_sel = int(input("Select Bank: "))
            if bank_sel < 1 or bank_sel > 7:
                print("You can only send to the displayed banks.")
            else:
                amount = float(input("Amount to transfer - #"))
                if amount > balance:
                    print("Insufficient funds. Please try a smaller amount.")
                elif amount <= 100:
                    print("Invalid! Minimum amount - #100.")
                else:
                    user_trans_pin = input("Enter transaction pin: ")
                    print("Processing Transaction. Please Wait.")
                    time.sleep(0.5)
                    if user_trans_pin != trans_pin:
                        print("Invalid Pin. Transaction cancelled.")
                    else:
                        if bank_sel != 4:  # If not Acex Bank
                            charges = amount * 0.015  # 1.5% interbank charges
                            print(f"Fee: #{charges:,.2f} deducted for interbank transfer.")
                            balance -= (amount + charges)

                        else:
                            balance -= amount

                        ref = "TXN" + str(random.randint(10000000, 99999999))
                        timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
                        print(f"""
                        {"=" * 40}
                        {"**TRANSACTION RECEIPT**".center(40)}
                        {"=" * 40}
                        Date & time        = {timestamp}
                        Reference No.      = {ref}
                        Amount transferred = #{amount:,.2f}
                        Recipient Account  = {recipient_acct_no}
                        New balance        = #{balance:,.2f}
                        {"-" * 40}
                        {"Thanks for banking with us!".center(40)}
                        {"Powered by Acex_Dev Team ©️".center(40)}
                        {"=" * 40}
                        """)
        post_action()
        action = input("> ")
        if action == "1":
            break
        else:
            continue
    return balance














