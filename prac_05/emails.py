"""
Word Occurrences
Estimate: 25 minutes
Actual:   43 minutes
"""


def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ('', 'y'):
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    name_part = email.split('@')[0]
    name_words = name_part.split('.')
    return ' '.join(name_words).title()


main()
