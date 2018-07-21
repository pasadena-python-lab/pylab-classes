"""
    Pylab 15 Oct 2016
    "Let's look at Pasadena Police PD service calls"

    Data source: Pasadena Open Data Portal
    http://data.cityofpasadena.net/datasets/pd-calls-for-service

    Also of interest : Pasadena PD Twitter Feed
    https://twitter.com/pasadenapd?lang=en

    Pasadena Crime mapping
    https://www.crimemapping.com/map/agency/284#

    Nathan @nate_somewhere

    Class notes:

    Python3 required, python2 not guaranteed to work completely
    Internet connection required
    Text editor required
"""


import os
import csv

try:
    # python3 functionality
    from urllib.request import urlretrieve
except ImportError as ex:
    from urllib import urlretrieve # python2 compability

url_csv = "https://opendata.arcgis.com/datasets/14b6c8deba7c4bb588b8687c5d0e8065_0.csv"
csv_filename = "pasadena_pd_service_calls.csv"

def file_downloader(url, filename):
    """Downloads and names a file given a filename and download_url"""

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print('File: %s downloaded' % filename)
    if os.path.isfile(filename):
        print('File: %s present and ready to go!' % filename)

    return os.path.abspath(filename)

# Open the CSV FILE
def read_csv_file(csv_filename):
    """ Opens csv file"""
    list_of_lists = []
    with open(csv_filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            list_of_lists.append(row)
    return list_of_lists

# Questions

# 1. Using python, how many incidents are this CSV?
# 2. What is the header row?

# More Difficult
# 3. How many 'TRAFFIC STOP' incident_type are in the csv?
# Hint - What is a for-loop in python?
# How would you count these?

# Bonus
# How many incidents of each type are in this dataset?
# Hint - Make a counter or find one available in python

# Extra Bonus
# Can you parse the incident_datetime timestamp?
# Hint: look into datetime.strptime

if __name__ == '__main__':
    print('hello world')

    ## Advanced - what is '__main__' and why does this work?


    ## uncomment after hello world runs
    csv_path = file_downloader(url_csv, csv_filename)

    ## uncomment when ready
    csv_data = read_csv_file(csv_path)

    # print(len(csv_data))

    # 1. Using python, how many incidents are this CSV?
    # header = csv_data[0]
    # print(header)

    all_incidents = csv_data[1:]

    # print(len(all_incidents))

    # 2. What is the header row?
    #
    # More Difficult
    # 3. How many 'TRAFFIC STOP' incident_type are in the csv?

    counter = 0
    for row in all_incidents:
        # print(repr(row[1]))
        if 'TRAFFIC STOP' in row[1]:
            # print('found')
            counter = counter + 1

    print(counter)
