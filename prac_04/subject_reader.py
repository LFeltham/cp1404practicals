"""#
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_data()
    display_subject_details(subjects)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject.append(parts)
    input_file.close()
    return subject


def display_subject_details(subject):
    for subject in subject:
        print()
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
