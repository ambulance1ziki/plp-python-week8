"""
Personal Mini-Toolkit
A menu-driven program with a calculator, a to-do list, and a number game.
"""

import random


def simple_calculator():
    # This tool performs addition, subtraction, multiplication, or division.
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers. Returning to the main menu.")
        return

    operation = input("Choose an operation (+, -, *, /): ").strip()

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You cannot divide by zero.")
            return
        result = first_number / second_number
    else:
        print(f"'{operation}' is not a supported operation.")
        return

    print(f"Result: {first_number:g} {operation} {second_number:g} = {result:g}")


def todo_list(tasks):
    # This tool allows the user to add, view, and remove tasks from a list.
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("A task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Removed: {removed_task}")
                else:
                    print("That task number is not on the list.")
            except ValueError:
                print("Please enter a whole number.")
        elif choice == "4":
            print("Returning to the main menu.")
            break
        else:
            print("Invalid to-do list option. Please choose 1, 2, 3, or 4.")


def number_guessing_game():
    # This tool gives the user clues until they guess the secret number.
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 20)
    attempts = 0

    print("I am thinking of a number from 1 to 20.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 20:
            print("Choose a number between 1 and 20.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"Correct! You guessed {secret_number} in {attempts} attempt(s).")
            break


def main():
    # The main loop keeps showing the menu until the user chooses Quit.
    tasks = []

    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n========== PERSONAL MINI-TOOLKIT ==========")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list(tasks)
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("Thank you for using the Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"'{choice}' is not a valid menu choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
