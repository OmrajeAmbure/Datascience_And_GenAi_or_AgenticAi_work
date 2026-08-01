# Reading CSV Files
# CSV (Comma-Separated Values) is widely used for storing tabular data. Python’s csv module helps parse CSV easily. Here, instead of needing an external file, we’ll simulate one using io.StringIO.
import csv
import io
csv_data = """
Year,Industry,Value
2014,Manufacturing,769400
2014,Manufacturing,48000
2014,Manufacturing,12
"""
csvfile = io.StringIO(csv_data)
csvreader = csv.reader(csvfile)
for row in csvreader:
    print(row)

"""
Explanation: Instead of a physical file, we used StringIO to create a file-like object. The CSV reader parses each line into a list of values.
"""