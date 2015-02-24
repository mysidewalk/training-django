# Bring in the Path library
from path import Path

# Create a variable to store my Path for OCD divisions
ocds = Path('/Users/peterfreeze/Sites/ocd-division-ids')

# Create 2 variables, one for storing the calculated size (reduces amount of calculation calls
# that have to be made). And another for storing the actual file
smallest_file_size = None
smallest_file = None

# Walk through each file for every directory within my Path, defined by what we declared on ln:5
# We are also filtering to make sure we only match ".csv" files to prevent contaminating our results
for csv_file in ocds.walkfiles('*.csv'):
    # On the first iteration, the first condition will be met (wrapped in parenthesis). We have not
    # yet set a smallest file size so it will ignore the second half of the "or" condition. 
    # Still on the first iteration, it will assign the file and size to their variables, and move
    # to the second iteration. The second and all subsequent iterations should fail the first
    # condition, allowing the second one to calculate and help find the smallest file.
    if (smallest_file_size is None) or (csv_file.getsize() < smallest_file_size):
        # If the file in the current iteration is smaller by size, we will reassign the
        # "smallest" variables
        smallest_file = csv_file
        smallest_file_size = csv_file.getsize()

# A safety check to make sure that we defined smallest_file before calling several methods on what
# we expect to be a file.
if smallest_file:
    print "Smallest file by size:"
    print "Location:",  smallest_file.parent
    print "Name:", smallest_file.name
    print "Size:", smallest_file_size
    print "Content:", smallest_file.lines()