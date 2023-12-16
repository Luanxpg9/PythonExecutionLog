import subprocess
import logging
import sys
import os

# Constants
LOG_FILE = 'executionLog.log'

logging.basicConfig(filename='executionLog.log', encoding='utf-8', level=logging.INFO)

def callError(errorMessage):
    print(errorMessage)
    logging.critical(errorMessage)

# If code has more than one argument don't go futher
if (sys.argv.__len__() != 2):
    callError("You can only pass the filename of the file you want to run in this project.\n Check Readme.txt for more details")

# Save the filename for the file to be executed
fileToExecute = sys.argv[1]

# Checks if the given file exists
if (os.path.isfile(fileToExecute)):
    callError("The filename you passed does not correspond to a file")

# Call a subprocess to execute the file and capture it's output
result = subprocess.run(
    ["py", fileToExecute], 
    capture_output=True, 
    text=True,
    check=True
)

# Split the output in lines
lines = result.stdout.splitlines()

# Save the output lines to a log file
for line in lines:
    print("Debug:", line)
    logging.info(line)