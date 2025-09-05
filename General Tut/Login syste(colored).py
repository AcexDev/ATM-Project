import json
import time
import sys
from colorama import Fore, Style, init

# initialize colorama
init(autoreset=True)


def initiate():
    print(f"""
{Fore.CYAN + "=" * 30}
{Fore.YELLOW}WELCOME TO ACEX LOGIN SYSTEM!
{Fore.CYAN + "=" * 30}\n
{Fore.GREEN}Choose an Option:
{Fore.CYAN}1 - Login
{Fore.CYAN}2 - Sign Up
{Fore.RED}* Any other key to exit
{Fore.CYAN + "-"*30}
    """)

with open("users.json", "r") as f:
    user_details = json.load(f)


def credentials_validate():
    print(Fore.YELLOW + "== LOGIN ==")
    username = input(Fore.CYAN + "Enter username: ")
    passcode = input(Fore.CYAN + "Enter passcode: ")

    for persons in user_details['users']:
        if username == persons['username'] and passcode == persons['passcode']:
            print(f"\n{Fore.GREEN}Access Granted ✅")
            time.sleep(0.5)
            print(f"{Fore.MAGENTA}Welcome back {persons['username']}!")
            return
    print(Fore.RED + "❌ No matching credentials found")


def registration():
    print(Fore.YELLOW + "== SIGN UP ==")
    new_user = {}
    username = input(Fore.CYAN + "Enter username: ")
    for persons in user_details['users']:
        if username == persons['username']:
            print(Fore.RED + "❌ Name already taken")
            return
        else:
            new_user['username'] = username

    while True:
        passcode = input(Fore.CYAN + "*Set passcode(4-digits): ")
        if not passcode.isdigit() or len(passcode) != 4:
            print(Fore.RED + "❌ Invalid! Passcode should be 4 digits")
        else:
            new_user['passcode'] = passcode
            print(Fore.YELLOW + "Processing..")
            time.sleep(1.5)
            user_details['users'].append(new_user)
            with open("users.json", "w") as db:
                json.dump(user_details, db, indent=2)
            print(f"\n{Fore.GREEN}✅ New User Successfully Created!")
            print(f"{Fore.CYAN}Redirecting to Login\n{'-'*30}\n")
            time.sleep(1.5)
            credentials_validate()
            break


def main():
    while True:
        initiate()
        choice = input(Fore.YELLOW + "> ")
        if choice == "1":
            credentials_validate()
        elif choice == "2":
            registration()
        else:
            sys.exit(Fore.RED + "Program exited")
        print(Fore.CYAN + "Redirecting to Main Menu..")
        time.sleep(1.5)
        print()

main()
