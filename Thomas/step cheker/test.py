file_path = 'C:/Users/tnj70/Desktop/Data/steps.txt'
done_steps = [0]  

def parse_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    dependencies = {}
    for line in lines:
        parts = line.strip().split(';')
        step_id = int(parts[0])
        dependencies[step_id] = [int(dep) for dep in parts[6].split('*')[0:]]
    return dependencies

def next_possible_steps(done_steps, dependencies):
    possible_steps = set()
    for step in done_steps:
        possible_steps.update(dependencies.get(step, []))
    possible_steps.difference_update(done_steps)  # Remove steps that have already been done
    return sorted(list(possible_steps))

def main():
    dependencies = parse_text_file(file_path)
    
    
    if not done_steps:
        initial_possible_steps = [step for step, dep in dependencies.items() if -1 in dep]
        print("Initial possible steps:", initial_possible_steps)
    else:
        possible_steps = next_possible_steps(done_steps, dependencies)
        new_possible_steps = []
        for step in possible_steps:
            new_possible_steps.extend(dependencies.get(step, []))
        
        new_possible_steps = list(set(new_possible_steps).difference(set(done_steps)))
        
        if not new_possible_steps:
            print("All steps are done.")
        else:
            print("Next possible steps:", new_possible_steps)

if __name__ == "__main__":
    main()