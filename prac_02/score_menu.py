def main():
    score = get_valid_score()
    choice = ""

    while choice != "Q":
        print_menu()
        choice = input("Enter your choice: ").strip().upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
        else:
            print("Invalid choice. Please select G, P, S, or Q.")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    score = -1
    while not (0 <= score <= 100):
        score_input = input("Enter a score (0-100): ")
        score = float(score_input)
    return score


def show_stars(score):
    num_stars = int(score)
    print("*" * num_stars)


def print_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


main()
