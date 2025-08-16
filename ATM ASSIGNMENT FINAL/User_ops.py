import time
import random

def generate_acct_number():
    return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"


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

def pin_change(trans_pin):
    print("=== ATM PASSWORD CHANGE MENU ===".center(40))
    old_pin = input("Enter your current PIN: ").strip()

    if old_pin == trans_pin:
        while True:
            new_pin = input("\nEnter new PIN (4 digits): ").strip()

            if new_pin == old_pin:
                print("❌ PIN already in use. Try another.")
                continue

            if len(new_pin) != 4 or not new_pin.isdigit():
                print("❌ Invalid PIN. It must be exactly 4 digits.")
                continue

            new_confirm = input("Re-confirm new PIN: ").strip()

            if new_confirm == new_pin:
                print("✅ PIN Change Successful!")
                return new_pin
            else:
                print("❌ PIN mismatch. Try again.")
    else:
        print("❌ Current PIN incorrect.")
        return trans_pin


def profile_view(profile):
    for field, details in profile.items():
        print(f"{field:<18}: {details}")


def profile_edit():
    while True:
        print("""
=== Profile Edit ️️✏️ ===
What would you like to edit?
1. Name\n2. Account Type\n3. Phone\n4. Email\n5. Return to Menu       
              """)
        choice = input("> ").strip()
        if choice == "1":
            profile['Name'] = input("Enter your name: ").strip()
            time.sleep(0.5)
            print("✅ Name successfully edited.")

        elif choice == "2":
            acct_type = input("Enter account type (Savings/Current): ").strip().capitalize()
            if acct_type in ["Savings", "Current"]:
                profile['Account Type'] = acct_type
                time.sleep(0.5)
                print("✅ Account type successfully edited.")
            else:
                print("❌ Invalid account type.")

        elif choice == "3":
            phone = input("Enter your phone number: ").strip()
            if phone.isdigit() and len(phone) == 11:
                profile['Phone'] = phone
                time.sleep(0.5)
                print("✅ Phone number successfully edited.")
            else:
                print("❌ Invalid! Enter an 11-digit Nigerian phone number.")
        elif choice == "4":
            profile['Email'] = input("Enter your valid Personal email account.")
            time.sleep(0.5)
            print("Email successfully edited ✅.")
        elif choice == "5":
            print("Returning to User Menu...")
            break
        else:
            print("Invalid! Please choose between 1 to 5.")

def user_menu_display():
    print(f"""
=== USER MENU ===
1 - View Profile
2 - Edit Profile
3 - Change Pin
4 - Return to Dashboard
""")


def profile_actions(trans_pin):
    while True:
        user_menu_display()
        cmd = input("> ").strip()
        try:
            if cmd == "1":
                print("---Profile---👤".center(30))
                profile_view(profile)
            elif cmd == "2":
                profile_edit()
            elif cmd == "3":
                new_pin = pin_change(trans_pin)
                return new_pin
            elif cmd == "4":
                time.sleep(1.0)
                return trans_pin
            else:
                print("Invalid! Options are between 1 to 3.")
        except ValueError:
            print("Invalid")
