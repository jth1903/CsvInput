import csv
import os

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
