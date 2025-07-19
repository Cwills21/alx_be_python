# pattern_drawing.py

# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Check if the input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the row counter
    row = 0

    # Outer while loop for rows
    while row < size:
        # Inner for loop for columns (asterisks in a row)
        for col in range(size):
            print("*", end="")

        # Print a newline after each row
        print()

        # Move to the next row
        row += 1
