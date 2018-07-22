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
    data = []
    with open(csv_filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            data.append(row)
    return data



if __name__ == '__main__':
    print('hello world')

    ## Advanced - what is '__main__' and why does this work?


    ## uncomment after hello world runs
    csv_path = file_downloader(url_csv, csv_filename)

    ## uncomment when ready
    csv_data = read_csv_file(csv_path)


    # Questions

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

    # Bonus
    # How many incidents of each type are in this dataset?
    # Hint - Make a counter or find one available in python

    # use a dictionary to store and for easy lookups
    all_incident_counter = {}

    for row in all_incidents:
        incident_type = row[1]

        # remove whitespace from the the incident_type
        incident_type_clean = incident_type.strip()
        # see the repr (what the computer sees)
        # print(repr(incident_type_clean))

        # see if the incident_type is in the counter
        if all_incident_counter.get(incident_type_clean):
            all_incident_counter[incident_type_clean] += 1
        else:
            # if not, then add it with starting value of 1
            all_incident_counter[incident_type_clean] = 1

    # see the count
    print(all_incident_counter)

    # Extra Bonus
    # Can you parse the incident_datetime timestamp?
    # Hint: look into datetime.strptime

    # sample timestamp
    str_time = "2017-11-17T22:02:37.000Z"

    # use the datetime library
    # learn the time formats here:
    # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

    import datetime
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    date_date = datetime.datetime.strptime(str_time, date_format)
    print(date_date)

    # Advanced Advice: use dateutil parser
    # https://dateutil.readthedocs.io/en/stable/parser.html
