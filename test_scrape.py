# Library for opening url and creating
# requests
import urllib.request

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present
# on the website
from html_table_parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd


# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):
    # Opens a website and read its
    # binary contents (HTTP Response Body)

    # making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    # reading contents of the website
    return f.read()


# defining the html contents of a URL.
xhtml = url_get_contents('https://www.depts.ttu.edu/communications/emergency/coronavirus/').decode('utf-8')

# Defining the HTMLTableParser object
p = HTMLTableParser()

# feeding the html contents in the
# HTMLTableParser object
p.feed(xhtml)

# Now finally obtaining the data of
# the table required
newTable = p.tables
#finTable = newTable.remove(newTable[0])
#print(finTable)
pprint(p.tables)

# converting the parsed data to
# datframe
print("\n\nPANDAS DATAFRAME\n")
dataFrame = pd.DataFrame(data=p.tables[0])
nDataFrame = dataFrame.drop(0)
print(nDataFrame)
#print(pd.DataFrame(p.tables))

nDataFrame.to_csv('TTU_COVIDNUMS.csv', index=False, header=False)

