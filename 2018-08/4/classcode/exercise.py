"""
    Pylab 4 Aug 2016
    "Scraping Craigslist for Apartment Lists"

    Data source: Craigslist RSS
    https://losangeles.craigslist.org/search/apa?availabilityMode=0&format=rss&query=pasadena

    Nathan @nate_somewhere

    Class notes:

    Python3 required, python2 not guaranteed to work completely
    Internet connection required
    Text editor required
"""


import os
from datetime import datetime
import re

try:
    # python3 functionality
    from urllib.request import urlretrieve
except ImportError as ex:
    from urllib import urlretrieve # python2 compability


def file_downloader(url, filename):
    """Downloads and names a file given a filename and download_url"""

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print('File: %s downloaded' % filename)
    if os.path.isfile(filename):
        print('File: %s present and ready to go!' % filename)

    return os.path.abspath(filename)

def open_file(file_path):
    """Opens a file and returns the data"""
    with open(file_path, 'r') as f:
        data = f.read()

    return data


url = "https://losangeles.craigslist.org/search/apa?availabilityMode=0&format=rss&query=pasadena"
str_time = datetime.now().strftime("%Hh-%Y-%m-%d")
filename = str_time + '.txt'


if __name__ == '__main__':

    file_location = file_downloader(url, filename)

    file_data = open_file(file_location)

    # Use regular expressions to pull out the listing URLs
    # Documentation : https://docs.python.org/3/library/re.html
    # ATBS Link : https://automatetheboringstuff.com/chapter7/

    # Find all of the page links
    pattern = re.compile(r'<item rdf:about=.*">')
    result = pattern.findall(file_data)

    # EXERCISE - Get all of the titles and images out for each listing
    # Return a list of dictionaries with the link, image links and title for each listing

    # Hints:
    # 1. How are each of the listing grouped in the XML?
    # 2. How can you identify the tags for images and titles for each?


    # EXERCISES - Advanced
    # 1. Can you add description to the data structure above?
    # 2. How can we add a filter by keywords in the description and title? Say I want only studio appartments


    # EXERCISE - Real World Applied
    # 1. How can we set up this script to run once an hour?
    # 2. How can we email out the results once an hour?

    # Hints:

    # Email
    # https://docs.python.org/3.4/library/email-examples.html
    # ATBS : https://automatetheboringstuff.com/chapter16/

    # Automate once an hour
    # One approach: https://www.tutorialspoint.com/python/time_sleep.htm
    # Other approach: google "cronjob"
