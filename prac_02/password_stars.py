MINIMUM_LENGTH = 4
# def original():
#     password = input(f"Enter password: ")
#     while len(password) < MINIMUM_LENGTH:
#         password = input(f"Enter password: ")
#     print('*' * len(password))
#

def main():
    password = get_password(MINIMUM_LENGTH)
    asterisks_for_password(password)


def get_password(minimum_length):
    password = input(f"Enter password: ")
    while len(password) < minimum_length:
        print(f"Password too short, must be at least {minimum_length} characters: ")
        password = input(f"Enter password: ")
    return password


def asterisks_for_password(sequence):
    print('*' * len(sequence))


main()
