"""
Word Occurrences
Estimate: 30 minutes
Actual:   22 minutes
"""
FILENAME = "wimbledon.csv"
COUNTRY_NUMBER = 1
CHAMPION_NUMBER = 2


def main():
    records = extract_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    champion_score = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_NUMBER])
        try:
            champion_score[record[CHAMPION_NUMBER]] += 1
        except KeyError:
            champion_score[record[CHAMPION_NUMBER]] = 1
    return champion_score, countries


def display_results(champion_score, countries):
    print("Wimbledon Champions: ")
    for name, count in champion_score.items():
        print(name, count)
    print(f"\nThese {len(countries)} Countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def extract_records(filename):
    records = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
