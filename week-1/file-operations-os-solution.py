# From exercise 2 in W1D3.md

# Import sys and os libraries
import sys
from platform import os

# The PYTHONPATH which is referenced in sys.path indicates the list of strings that specifies the
# search path for modules that have been installed.
python_path = sys.path

# Using the os class, we can find out our current working directory and store that
current_directory = os.getcwd()

# We can include this in our path by appending it to the list we found earlier
python_path.append(current_directory)

# When creating python files that can run, we can allow them to take arguments by using the sys
# library and accessing the "argv" property. The "argv" property is a list of all of the arguments
# passed to the current script. You can see this by running "python file-operations-os-solution.py"
# from your terminal to see the file name called when executing this. Adding "--note" would include
# it in the list of arguments.
arguments = sys.argv
print arguments
