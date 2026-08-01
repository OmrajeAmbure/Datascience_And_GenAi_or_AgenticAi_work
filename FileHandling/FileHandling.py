import os

"""
📝 Need for File Handling
    - Store data permanently, even after the program ends.
    - Access external files like .txt, .csv, .json, etc.
    - Process large files efficiently without using much memory.
    - Automate tasks like reading configs or saving outputs.

'r' open for reading (default)
'w' open for writing, truncating the file first
'x' create a new file and open it for writing
'a' open for writing, appending to the end of the file if it exists
'b' binary mode
't' text mode (default)
'+' open a disk file for updating (reading and writing)
"""


# 1. Open The File using open() Function
file = open("tex.txt", "r") # he default mode is 'rt' (open for reading text)

# Read File By using following function :- 
print(file.read(5)) # Read The Entire Text From The File or specified character  
print(file.readline()) # Read The First Line or specificed character 
print(file.readable()) # Return whether object was opened for reading.If False, read() will raise OSError.
print(file.readlines()) # Return a list of lines from the stream. ex., ['hello this is demo file\n', 'line2\n', 'line3']

file.close()

for line in file:
    print(line.strip())


line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
file.close()

# Using with Statement
# Instead of manually opening and closing the file, you can use the with statement, which automatically handles closing. This reduces the risk of file corruption and resource leakage.
with open("tex.txt", "r") as file1:
    content = file1.read()
    print(content)
    file1.close()

"""
Different File Mode in Python
Below are the different types of file modes in Python along with their description:

Mode

Description

‘r’	    Read-only. Raises I/O error if file doesn't exist.
‘r+’	Read and write. Raises I/O error if the file does not exist.
‘w’	    Write-only. Overwrites file if it exists, else creates a new one.
‘w+’	Read and write. Overwrites file or creates new one.
‘a’	    Append-only. Adds data to end. Creates file if it doesn't exist.
‘a+’	Read and append. Pointer at end. Creates file if it doesn't exist.
‘rb’	Read in binary mode. File must exist.
‘rb+’	Read and write in binary mode. File must exist.
‘wb’	Write in binary. Overwrites or creates new.
‘wb+’	Read and write in binary. Overwrites or creates new.
‘ab’	Append in binary. Creates file if not exist.
‘ab+’	Read and append in binary. Creates file if it does not exist.

"""

# 2. Writing to file in Python
"""
Mode / Option	        Description
"w"	            Write mode: creates file if missing, truncates (erases) if it exists
"a"	            Append mode: creates file if missing, writes data always at the end
"x"	            Exclusive create: creates new file, but fails with FileExistsError if it already exists
"b"	            Binary flag: used with other modes (e.g., "wb", "ab") for binary files
"+"	            Read/write flag: combine with other modes (e.g., "r+", "w+") for both reading and writing
encoding=	    Specify text encoding (e.g., "utf-8") when working with text files
newline=	    Control newline translation in text mode (e.g., "\n")
"""

