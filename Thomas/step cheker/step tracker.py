file_path = "C:/Users/tnj70/Desktop/Data/steps.txt"  # Change this to the path of your text file

def read_steps_from_file(file_path):
    with open(file_path, 'r') as file:
        steps = [line.strip().split(';') for line in file.readlines()]
    return steps

def display_current_step(steps, current_step, total_steps):
    step_info = steps[current_step - 1][1:]  # Exclude the step number
    print(f"Step {current_step}/{total_steps}:")
    print(f"  Color: {step_info[0]}")
    print(f"  Brick Type: {step_info[1]}")
    print(f"  Position: {step_info[2]}")
    print(f"  Rotation: {step_info[3]}")
    print(f"  Grit Size: {step_info[4]}")
    print(f"  Grit Position: {step_info[5]}")
    print(f"  Previous Step: {step_info[6]}")

def main():
    steps = read_steps_from_file(file_path)

    if steps is not None:
        total_steps = len(steps)
        current_step = 1

        while current_step <= total_steps:
            display_current_step(steps, current_step, total_steps)
            current_step += 1


if __name__ == "__main__":
    main()
