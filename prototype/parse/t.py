import json
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})


def parse_markdown_to_json(file_path):
    # Read the Markdown file
    with open(file_path, "r") as file:
        content = file.read()

    # Split the content into sections
    sections = content.split("\n\n##")

    # Create a dictionary to store the parsed data
    data = {}

    # Iterate over the sections and extract the data
    for section in sections:
        # Split the section into title and description
        split_index = section.find("\n\n")
        if split_index != -1:
            title = section[:split_index].strip().lower().replace(" ", "_")
            description = section[split_index + 2 :].strip()
            data[title] = {"description": description}

    return data


# Specify the path to the Markdown file
markdown_file_path = "t.md"

# Parse the Markdown file and format it into JSON
parsed_data = parse_markdown_to_json(markdown_file_path)

jdb.i(parsed_data)
jdb.print()
