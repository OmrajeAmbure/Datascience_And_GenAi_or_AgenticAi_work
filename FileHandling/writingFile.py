"""
Encoding file handling is the process of managing how human-readable characters and 
data are translated into raw binary bytes when saving to a file, and back into text when reading it back

Core Concepts
    - Bytes vs. Characters: Computers only understand numbers (bytes), while humans read letters and symbols. Encoding acts as the dictionary or map between the two.
    - Common Encodings:UTF-8: The modern global standard. It supports almost all world languages, emojis, and is backward-compatible with ASCII.
    - ASCII: An older, basic 7-bit standard that only covers standard English letters, numbers, and basic symbols.
    - Windows-1252 / Latin-1: Older regional encodings often found in legacy Windows or text documents.
    - Why It Matters in Programming: If you try to read a file using the wrong encoding (like trying to read a Windows-1252 file with standard UTF-8 settings), your program will crash with a decoding error or display broken characters.

# 2. Writing to file in Python

Mode / Option	        Description
"w"	            Write mode: creates file if missing, truncates (erases) if it exists
"a"	            Append mode: creates file if missing, writes data always at the end
"x"	            Exclusive create: creates new file, but fails with FileExistsError if it already exists
"b"	            Binary flag: used with other modes (e.g., "wb", "ab") for binary files
"+"	            Read/write flag: combine with other modes (e.g., "r+", "w+") for both reading and writing
encoding=	    Specify text encoding (e.g., "utf-8") when working with text files
newline=	    Control newline translation in text mode (e.g., "\n")
"""
with open('write.txt','w+',encoding="utf-8") as file: # (write + read) mode open this file
    print(file.write("This first line of wirting file \n")) # Write string s to stream. Return the number of characters written. Overwrite the existing test in file
    print(file.write("This second line \n"))
    # print(file.read())
    file.close()

with open("write.txt", "r", encoding="utf-8") as f:
    print(f.read())
    f.close()

with open("write.txt",'a',encoding="utf-8") as file:
    print(file.write("write append new line this text"))  # Write string s to stream. Return the number of characters written. do not Overwrite the existing test in file
    file.close()

with open("write.txt", "r", encoding="utf-8") as f:
    print(f.read())


# Create only if it does not exist
# With "x" mode, Python creates a new file but raises FileExistsError if the file already exists. This prevents accidental overwrites.
try:
    with open("file.txt", "x", encoding="utf-8") as f:
        f.write("Created using exclusive mode.\n")
except FileExistsError:
    print("file.txt already exists, exclusive creation aborted.")

# Writing multiple lines
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("file1.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

with open("file1.txt", "r", encoding="utf-8") as f:
    print(f.read())


# Writing to a Binary File
# For non-text data (like images, audio, or other binary content), use binary write mode ("wb"). This treats the file as raw bytes instead of text.
data = b'\x00\x01\x02\x03\x04'
with open("file.bin", "wb") as f:
    f.write(data)