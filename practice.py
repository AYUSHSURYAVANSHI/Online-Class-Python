# 2. Write a program to read 3 float numbers from the keyboard with, seperator and print their sum?

# ans:

def main():
    # Prompt the user to enter three float numbers separated by a specified separator
    input_string = input("Enter three float numbers separated by a space: ")
    
    # Split the input string into a list of strings
    numbers_str = input_string.split()
    
    # Convert the list of strings to a list of floats
    try:
        numbers = [float(num) for num in numbers_str]
        
        # Check if exactly three numbers were entered
        if len(numbers) != 3:
            print("Please enter exactly three float numbers.")
            return
        
        # Calculate the sum of the numbers
        total_sum = sum(numbers)
        
        # Print the sum
        print(f"The sum of the numbers is: {total_sum}")
    
    except ValueError:
        print("Please enter valid float numbers.")

if __name__ == "__main__":
    main()