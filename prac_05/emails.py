def main():
    email_to_name = {}
    email = input("Enter your email address: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Enter your name: ")
        email_to_name[email] = name
        email = input("Enter your email address: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")
