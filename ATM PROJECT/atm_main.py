from atm_functions import (
    initialize_atm, login_sequence, display_main_menu,
    check_balance, handle_withdrawal, handle_deposit
)
import time
import sys

# === Program Starts ===
initialize_atm()
login_sequence()

balance = 200000
trans_pin = "1234"

while True:
    time.sleep(1.5)
    display_main_menu()
    command = input("> ")

    if command == "1":
        check_balance(balance)
    elif command == "2":
        balance = handle_withdrawal(balance, trans_pin)
    elif command == "3":
        balance = handle_deposit(balance, trans_pin)
    elif command == "4":
        print("✅ Session Ended. Please take your Card 💳.\nThank you for using ACEX_DEV ATM. Stay safe!")
        sys.exit()
    else:
        print("Invalid option. Please choose 1-4")

    time.sleep(0.3)
    print("\n**REDIRECTING TO DASHBOARD. PLEASE WAIT!**")
