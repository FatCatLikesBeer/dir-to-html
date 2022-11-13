#!/usr/bin/env python3

#####
#
# dir_to_html.py
# © Billy Bagel 2022
#
#####

"""
This script outputs a primitive HTML file with links to files.
It generates links by walking a top-directory and its contents (files and subdirs).
The top-directory is the directory this script is located in.
The output HTML lists directories and files in no particular order.
Does not work nicely when file & directory names inlude the following: spaces, special characters, emojis.
Place script at the top most directory you wish to walk.
'index.HTML' will be output in the same directory as this script.
Caution: This also outputs hidden files and directories.
"""

import os

# Declaring variables
dirAddress = os.getcwd()                # Set var to the script's current directory
prefix = os.path.join(dirAddress, "")   # Prefix to remove from generated URL
header = '<!DOCTYPE html>\n'            # Top and bottom html text blocks
header += '<html>\n'
header += '<head>\n'
header += '<title>Welcome to nginx!</title>\n'
header += '<style>\n'
header += '\tbody { \n\t\twidth: 35em; \n\t\tmargin: 0 auto; \n\t\tfont-family: Tahoma, Verdana, Arial, sans-serif;\n\t}\n'
header += '</style>\n'
header += '</head>\n'
header += '<body>\n'
footer = '</body>\n'
footer += '</html>'
body = []
verify = ""

# The os.walk() method has 3 outputs. First is directory path, then subdirectory names, then file names.
# The os.walk() method allows the walking of symlinks.
# The following for loop walks the directories, formats links & names, then saves to 'body' list var.
for dirPath, subDir, fileName in os.walk(dirAddress,followlinks=True):
    body += ('<h>',dirPath.removeprefix(prefix),'</h><br><br>','\n')        # Creates section titles.
    for i in sorted(fileName):
        body += ('<a href=/',dirPath.removeprefix(prefix),'/',i,'>',i,'</a>','<br><br>','\n')   # Creates links to files.
    body += ('<br>') # Break after each section.

# File handling, writing, and verification of tail end of body.
file = open('index.html','w')           # Open index.HTML
for i in header:                        # Write header
    file.write(i)
for line in body:                       # Write body
    file.write(str(line))
for line in body[-200:]:
    verify += line                      # Tail end of body to verifiy if script is working correctly
for i in footer:                        # Write footer
    file.write(i)
file.close()
print(verify)                           # Prints last few lines to verify proper formatting.
