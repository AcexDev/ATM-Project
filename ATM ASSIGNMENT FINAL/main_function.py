from atm_functions import (
    initialize_atm, login_sequence, display_main_menu,
    check_balance, handle_withdrawal, handle_deposit,
    avail_banks, transfer, post_action
)
from User_ops import (
    profile_view, generate_acct_number, profile_edit,
    user_menu_display, profile_actions, pin_change
)
import time
import sys

# === Program Starts ===


def run_dashboard(balance, trans_pin, profile):
    while True:
        time.sleep(1.5)
        display_main_menu()
        command = input("> ")

        if command == "1":
            check_balance(balance)
            time.sleep(0.3)
            print("\n**REDIRECTING TO DASHBOARD. PLEASE WAIT!**")

        elif command == "2":
            balance = handle_withdrawal(balance, trans_pin)
            time.sleep(0.3)
            print("\n**REDIRECTING TO DASHBOARD. PLEASE WAIT!**")

        elif command == "3":
            balance = handle_deposit(balance, trans_pin)
            time.sleep(0.3)
            print("\n**REDIRECTING TO DASHBOARD. PLEASE WAIT!**")

        elif command == "4":
            balance = transfer(balance, trans_pin)
            time.sleep(0.3)
            print("\n**REDIRECTING TO DASHBOARD. PLEASE WAIT!**")

        elif command == "5":
            trans_pin = profile_actions(trans_pin)

        elif command == "6":
            print("✅ Session Ended. Please take your Card 💳.\nThank you for using ACEX_DEV ATM. Stay safe!")
            sys.exit()

        else:
            print("Invalid option. Please choose 1-6")

