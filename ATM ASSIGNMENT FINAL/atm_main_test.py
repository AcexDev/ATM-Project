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
from main_function import run_dashboard

# === Program Starts ===
initialize_atm()
login_sequence()

balance = 200000
trans_pin = "1234"
user_name = "User"
acct_no = generate_acct_number()
acct_type = "Savings/Current"
user_phone = "______"
user_email = "______"

profile = {
    "Name": user_name,
    "Account Number": acct_no,
    "Account Type": acct_type,
    "Bank": "Acex Finance",
    "Phone": user_phone,
    "Email": user_email
}

run_dashboard(balance, trans_pin, profile)