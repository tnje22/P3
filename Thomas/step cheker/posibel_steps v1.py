# Read the data from the text file
with open('C:/Users/tnj70/Desktop/Data/steps.txt', 'r') as file:
    lines = file.readlines()

# dummi list to compare with
compare_list = [0, 1, 7, 9,]

# Keep track of lines with a match
steps_done = [] 

# Process each line in the data
for index, line in enumerate(lines):
    # Split the line using semicolons
    values = line.strip().split(';')
    
    # Extract the first value
    first_value = int(values[0])
    #last_value = int(values[6])

    # Compare with the list
    if first_value in compare_list:
        steps_done.append(index)  
# Close the file
file.close()

# Print the matching lines
print("step:", steps_done,"are done")

#print(last_value)