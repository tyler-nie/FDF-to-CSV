import re
import csv
filename = "fdf_to_convert.fdf"

def fdf_to_csv(fdf_data, csv_file):
    """
    Converts fdf to CSV
    Puts data into output.csv"""
    fdf_pattern = re.compile(r"/V\((.*?)\)/T\((.*?)\)", re.DOTALL)
    fields = fdf_pattern.findall(fdf_data)

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Value', 'Field Name'])
        for field in fields:
            writer.writerow(field)

def count_rows():
    """
    Counts the number of Fields
    """
    file = open('output.csv')
    row_count = len(file.readlines())
    print ("Number of Fields: ", (row_count-1))

def count_checked_boxes():
    """
    Counts the number of checked boxes"""
    word = "Yes"
    count = 0

    with open(filename, 'r', encoding='latin-1') as f:
        fdf_data = f.readlines()
        for line in fdf_data: 
            l = len(line)
            n = len(word)
            for i in range(l - n):
                if line[i] == word[0]:
                    if line[i:i+n] == word:
                        count += 1
    print("Number of checked boxes: ", count)      


# Read & Write files
csv_file = 'output.csv'

# Read FDF file
with open(filename, 'r', encoding='latin-1') as f:
    fdf_data = f.read()

# Convert data to CSV
fdf_to_csv(fdf_data, csv_file)

# Counts information we require
count_rows()
count_checked_boxes()
