import random


def main():
    score = float(input("Enter score: "))
    print(determine_result(score))

    random_score = random.uniform(0, 100)
    print(f"Generated random score: {random_score:.2f}")
    print(determine_result(random_score))


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
