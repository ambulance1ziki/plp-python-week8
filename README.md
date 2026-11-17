Personal Mini-Toolkit
What the toolkit does
The Personal Mini-Toolkit is a menu-driven Python program with three tools:
1. Simple Calculator — performs addition, subtraction, multiplication, and division.
2. To-Do List — allows users to add, view, and remove tasks while the program is running.
3. Number Guessing Game — asks the user to guess a randomly selected number from 1 to 20.
The project practices variables, input/output, conditionals, loops, lists, functions, comments, and f-strings.
Files
- toolkit_plan.txt — the plan written before building the program.
- toolkit.py — the complete Python program.
- screenshots/ — sample console captures showing the menu, invalid choice, and each tool in action.
How to run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this project folder.
3. Run:
   python toolkit.py
   On some systems, use python3 toolkit.py.
4. Choose an option from the menu and follow the instructions. Choose 4 to quit.
Reflection
The hardest part of this project was making the to-do list menu work independently while still returning to the main menu when requested. The bug that took the longest to fix was handling invalid number input without crashing the program. I used try and except so that incorrect input displays a helpful message instead of stopping the program. I also checked that the task list changes correctly when tasks are added or removed. The project helped me understand how functions, loops, lists, and conditionals work together in one program. If I had one more week, I would add a feature that saves tasks to a file so they are still available after the program closes.
