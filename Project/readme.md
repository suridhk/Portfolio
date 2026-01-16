# Introduction to Programming – Final Assignment

This repository contains the things we learned while doing our final assignment **Task 1** and **Task 2** and their solution.
Both tasks utilize **Python** and emphasize fundamental programming ideas like input validation, conditional statements, loops, and basic computations.

---

## Task 1: Beckett Pizza Plaza 

### Desciption
This script handles a **4-for-3** promotion deal. It computes the order total by spotting the least expensive pizza and deducting it as a discount.The customer must order **exactly four pizzas**, and the **cheapest pizza is free**.

The program:

- Asks the user to enter the price of only four pizzas.
- Checks inputs to confirm they are positive numbers.
- Determines final cost by excluding the lowest-priced pizza.
- Shows the total payable and discount percentage saved.

### Rules Applied

- Pizza prices require values above zero.
- Invalid non-numeric entries get rejected.
- Discount computation uses a percentage of the initial total.
- The highest allowable discount caps at 25%.
- Users cannot input pizza prices exceeding four.

### What I learned 

- How to use loops and to ensure exactly four valid inputs.
- How to store multiple values using a list.
- How locate the lowest value with min() on a list of numbers.
- Compute sums using sum() across iterable collections.
- Implement conditional logic via if/else statements to enforce business rules.
- Transform real-world problems by breaking into input, validation, calculation, and output steps.

---

## Task 2 : Password Security Check

### Description 
A security simulation that mimics **Partial Password** authentication, a common technique used by banking applications to prevent credential theft.

The program:

- - Asks the user to enter a password.
- Checks that the password is **at least 9 characters long**.
- If valid, asks the user to enter **three randomly chosen characters** from the password.
- If any character is incorrect, the program exits immediately.
- If all checks are confirmed, the security check passes.

### Rules Applied

- Passwords under 9 characters get rejected.
- Random positions can repeat.
- Program terminates right away on invalid input.

### What I learned 

- Determine string length using len().
- Apply if/else statements for input validation.
- Employ loops to perform repeated security verifications.
- Retrieve string characters via indexing [index].
- Create random integers with random.randint().
- Match user input against saved data.
- Halt program execution instantly with sys.exit().
- Develop basic password security validation.

---

## Technologies Used

- Python 3
- VS Code

---

## How to Run the Programs
1. Make sure Python 3 is installed
2. Open a terminal or command prompt
3. Navigate to the project folder  
3. Run the Python files using:
```bash
python task1.py
or
python task2.py