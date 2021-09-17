import csv
import os
import glob
from xlsxwriter.workbook import Workbook

folder_name = input('Please enter the name of the folder you would like to save your file to\n : ')
os.mkdir(folder_name)
os.chdir(folder_name)

rowcount = 0


def convert(string):
    li = list(string.split(', '))
    return li


file_name = input('please enter the name of the file you are creating.\n : ')

header = input('please enter the header row with units separated by commas and a space\n : ')


with open('{}.csv'.format(file_name), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(convert(header))
    newrow = input('Is there another row?\n')
    desiredcount = input('How many rows are there? (besides the header row)\n : ')
    while rowcount < int(desiredcount):
        if newrow == 'yes' or newrow == 'Yes' or newrow == 'y':
            values = input('please enter a list of values for the row separated by a comma and a space\n : ')
            writer.writerow(convert(values))
            rowcount += 1

for file in glob.glob(os.path.join('.', '*.csv')):
    workbook = Workbook(file[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(file, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()
