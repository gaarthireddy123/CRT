# task.py

import math

def calculate_result(name, grades):
    # Calculate average
    average = sum(grades) / len(grades)

    # Determine pass/fail
    status = "Pass" if average >= 40 else "fail"

    # Truncate to 2 decimal places (no rounding) to match expected output
    truncated = math.floor(average * 100) / 100

    if truncated == int(truncated):
        average_str = f"{truncated:.1f}"
    else:
        average_str = f"{truncated:.2f}".rstrip('0').rstrip('.')

    return f"Average grade: {average_str}, Status: {status}"


def Student_Grade_System(name, *grades):
    # allow either three numeric args or a grades iterable
    if len(grades) == 1 and isinstance(grades[0], (list, tuple)):
        grades = grades[0]

    return calculate_result(name, grades)


if __name__ == "__main__":
    # Input
    name = input("Enter student name: ")
    grades = list(map(int, input("Enter 3 subject grades separated by space: ").split()))

    # Output
    result = calculate_result(name, grades)
    print(result) 
