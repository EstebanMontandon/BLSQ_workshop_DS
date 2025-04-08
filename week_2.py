"""Git Exercise - Python Project.

This script is intended for educational purposes. It allows students to practice Git basics such as
cloning, branching, committing, solving conflicts, and more.

Students:
  - Paula (good Python level)
  - Leyre (good Python level)
  - Giulia (good Python level)
  - Rita (beginner in Python)
  - Michael (? Python level)

Instructions:
  - Each student should modify their assigned function according to the provided guidelines.
  - Create a branch with your name before modifying the code.
  - Commit your changes and push them to the repository.
  - Try to create conflicts by modifying shared parts of the code (e.g., the main function).
  - Resolve conflicts collaboratively.

"""


def greet_user(name: str) -> str:
    """Function assigned to Rita.

    Task: Improve this function by making the greeting more personalized.
    For example, allow the user to input their favorite hobby and include it in the greeting.

    Args:
        name (str): The name of the user.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the Git practice project."


def calculate_square(number: int) -> int:
    """Function assigned to Giulia.

    Task: Modify this function to support calculating squares of floats as well.
    Additionally, implement error handling for invalid inputs.

    Args:
        number (int): A number to be squared.

    Returns:
        int: The square of the input number.
    """
    return number**2


def is_even(num: int) -> bool:
    """Function assigned to Paula.
    Task: Improve this function to check if a number is even or odd.

    Args:
        num (int): The number to check.
    Returns:
        bool: True if the number is even, False otherwise.
    """
    if num % 2 == 0:
        return True
    else:
        return False


def find_max(numbers: list) -> int:
    """Function assigned to Leyre.

    Task: Modify this function to use Python native functions instead of a loop.

    Args:
        numbers (list): A list of numbers.
    Returns:
        int: The maximum number in the list.
    """

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def add_numbers(a: int, b: int) -> int:
    """Function assigned to Michael.

    Task: Write a function that takes two numbers and returns their sum..
    Additionally, implement error handling for string inputs. It can display a message like "Invalid input".
    Example: try: add_numbers("2", "3") except ValueError as e: print(f"Invalid input: {e}") return None
    Args:
        a (int): A number.
        b (int): A number.
    Returns:
        int: The sum of a and b.
    """
    return a + b


def main():
    """Main function to demonstrate all functionalities.

    Students may modify this function to test their changes.
    """
    print(greet_user("Student"))
    print(f"Square of 4: {calculate_square(4)}")
    print(f"Is 3 an even number : {is_even(3)}")
    print(f"Find max : {find_max([1, 3, 5])}")
    print(f"Add 2 + 2 : {add_numbers(2, 2)}")


if __name__ == "__main__":
    main()
