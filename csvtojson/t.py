import csv


def csv_to_dict(csv_file):
    data = {}

    with open(csv_file, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        current_key = ""
        current_subkey = ""
        current_stats = []

        for row in reader:
            if row[0].startswith("TYPE"):
                data["type"] = row[1]
            elif row[0].startswith("ARCHETYPE"):
                archetypes = [item.strip() for item in row[1:] if item.strip()]
                data["archetype"] = archetypes
            elif row[0].startswith("HISTORY"):
                history = []
                current_year = {}

                for item in row[1:]:
                    if item.startswith("year"):
                        if current_year:
                            history.append(current_year)
                            current_year = {}
                        current_year["desc"] = item.split(" desc\t")[1]
                    elif item.startswith("year") and "stats" in item:
                        stats = item.split("\t")[1].split(", ")
                        current_year["stats"] = [
                            [s.split()[0], int(s.split()[1])] for s in stats
                        ]

                if current_year:
                    history.append(current_year)
                data["history"] = history
            elif row[0].startswith("EVENTS"):
                events = []
                current_event = {}

                for item in row[1:]:
                    if item.startswith("title"):
                        if current_event:
                            events.append(current_event)
                            current_event = {}
                        current_event["title"] = item.split("\t")[1]
                    elif item.startswith("desc"):
                        current_event["desc"] = item.split("\t")[1]
                    elif item.startswith("choice desc"):
                        if "choices" not in current_event:
                            current_event["choices"] = []
                        choice = {"desc": item.split("\t")[1]}
                        current_event["choices"].append(choice)
                    elif item.startswith("choice stats"):
                        stats = item.split("\t")[1].split(", ")
                        current_choice = current_event["choices"][-1]
                        current_choice["stats"] = [
                            [s.split()[0], int(s.split()[1])] for s in stats
                        ]

                if current_event:
                    events.append(current_event)
                data["events"] = events
            elif row[0].startswith("BENEFITS"):
                benefits = [item.strip() for item in row[1:] if item.strip()]
                data["benefits"] = benefits
            elif row[0].startswith("QUITTING"):
                quitting = [item.strip() for item in row[1:] if item.strip()]
                data["quitting"] = quitting

    return data


# Specify the input CSV file path
csv_file_path = "A Life Chronicle Port, Character Generator - Sheet1.csv"

# Convert CSV to Python dictionary
result_dict = csv_to_dict(csv_file_path)

# Print the resulting Python dictionary
print(result_dict)
