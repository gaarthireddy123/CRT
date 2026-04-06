# task.py

def reverse_string(s):
    reversed_str = ""

    # Loop through string from end to start
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]

    return reversed_str


def Reverse_String(s):
    # Provide the expected function name for tests
    return reverse_string(s)


if __name__ == "__main__":
    user_input = input()
    print(Reverse_String(user_input))
