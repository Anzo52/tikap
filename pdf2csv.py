# Python program to convert pdf to csv using tika
# file path is passed as argument on command line
# output csv is saved in same directory as pdf


import sys
import os
import subprocess
import csv
import tika
from tika import parser


# parse pdf context and return list of lines
def tika_reader(file_path):
    raw_text = parser.from_file(file_path)
    raw_list = raw_text['content'].splitlines()
    return raw_list

# convert content to csv format
def tika_to_csv(file_path):
    raw_list = tika_reader(file_path)
    csv_list = []
    for line in raw_list:
        csv_list.append(line.split(','))
        # remove empty space at beginning of file
    csv_list.pop(0)
    return csv_list

# save to csv file
def tika_to_csv_file(file_path):
    csv_list = tika_to_csv(file_path)
    csv_file_path = os.path.splitext(file_path)[0] + '.csv'
    with open(csv_file_path, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(csv_list)
    return csv_file_path

def main():
    file_path = sys.argv[1]
    csv_file_path = tika_to_csv_file(file_path)
    print(csv_file_path)


if __name__ == '__main__':
    main()