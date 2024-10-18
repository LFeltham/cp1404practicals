import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(int(number_of_quick_picks)):
        quick_pick = []
        for j in range(int(NUMBERS_PER_LINE)):
            random_number = random.randint(MINIMUM, MAXIMUM)
            while random_number in quick_pick:
                random_number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(random_number)
        quick_pick.sort()
        print(" ".join(f"{random_number:2}" for random_number in quick_pick))


main()
