import re, os, csv


script_dicrecotry = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_dicrecotry, 'mergedfixed.tmx')
input_file_path = os.path.join(script_dicrecotry, 'merged.tmx')
term_file_path = os.path.join(script_dicrecotry, 'TermsToBeFixed.csv')


# Read the CSV file and create a dictionary mapping value1 to value2
value_mapping = {}
with open(term_file_path, 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        value_mapping[row[0]] = row[1]

# Read the text file and replace value1 with value2
with open(input_file_path, 'r', encoding='utf-8') as text_file:
    text = text_file.read()

    # Iterate over each key-value pair in the mapping dictionary
    for value1, value2 in value_mapping.items():
        # Replace all occurrences of value1 with value2 in the text
        text = text.replace(value1, value2)

# Write the modified text back to the text file
with open(output_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(text)

