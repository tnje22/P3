
completed_steps = []

def find_next_steps(file_path, completed_steps):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Convert steps into a dictionary for easy lookup
    steps_dict = {}
    for line in lines:
        step_info = line.strip().split(';')
        step_id = int(step_info[0])
        dependencies = [int(dep) for dep in step_info[-1].split('*')]
        steps_dict[step_id] = {'dependencies': dependencies, 'completed': False}

    # Find all possible next steps
    possible_next_steps = []
    for step_id, step_data in steps_dict.items():
        if not step_data['completed'] and (step_data['dependencies'] == [-1] or all(dep in completed_steps for dep in step_data['dependencies'])):
            possible_next_steps.append(step_id)

    # Filter out completed steps
    possible_next_steps = [step_id for step_id in possible_next_steps if step_id not in completed_steps]

    return possible_next_steps

# Dummy data
next_steps = find_next_steps('Thomas/step cheker/data/2.txt', completed_steps)

if next_steps:
    print(f"The possible next steps are: {next_steps}")
else:
    print("The construction is done")
