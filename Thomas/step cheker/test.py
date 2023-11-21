# Read the data from the text file
with open('C:/Users/tnj70/Desktop/Data/steps.txt', 'r') as file:
    lines = file.readlines()

# Process each line in the data
for index, line in enumerate(lines):
    # Split the line using semicolons
    values = line.strip().split(';')
    
    # Extract the first value
    first_value = int(values[0])

    # Extract the last value if it exists and is not empty
    last_value = int(values[-1]) if values[-1] and values[-1].isdigit() else None
    
    # Print the current line and its dependencies
    print(f"Line {index + 1}: {line.strip()} - Dependencies: ", end="")
    
    # Check if there is a valid last value
    if last_value is not None and 1 <= last_value <= len(lines):
        # Check if last_value - 1 is a valid index
        if 0 <= last_value - 1 < len(values):
            # Print the line numbers that the current line is dependent on, separated by (*)
            dependencies = values[last_value - 1].split('*')
            print("(*)".join(dependencies))
        else:
            print("Invalid index")
    else:
        print("None")

# Close the file
file.close()
