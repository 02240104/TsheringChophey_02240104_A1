import math
import re

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_number_sum(start, end):
    """Calculate the sum of prime numbers within a given range."""
    return sum(num for num in range(start, end + 1) if is_prime(num))

def length_converter(value, direction):
    """Convert length between meters and feet."""
    if direction == 'M':
        return round(value * 3.28084, 2)  # Meters to feet
    elif direction == 'F':
        return round(value / 3.28084, 2)  # Feet to meters
    else:
        return None

def consonant_counter(text):
    """Count the number of consonants in a string."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)

def min_max_finder(numbers):
    """Find the smallest and largest numbers in a list."""
    return min(numbers), max(numbers)

def palindrome_checker(text):
    """Check if a string is a palindrome (ignoring spaces and case)."""
    cleaned_text = re.sub(r'\s+', '', text).lower()
    return cleaned_text == cleaned_text[::-1]

def word_counter(file_path):
    """Count occurrences of specific words in a text file."""
    target_words = ["the", "was", "and"]
    word_counts = {word: 0 for word in target_words}
    
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
            for word in target_words:
                word_counts[word] = len(re.findall(r'\b' + re.escape(word) + r'\b', text))
        return word_counts
    except FileNotFoundError:
        return "File not found."

def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("1. Prime Number Sum Calculator")
    print("2. Length Unit Converter")
    print("3. Consonant Counter")
    print("4. Min-Max Number Finder")
    print("5. Palindrome Checker")
    print("6. Word Counter")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select a function (1-7): ").strip()
        
        if choice == '1':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            result = prime_number_sum(start, end)
            print(f"Sum of prime numbers between {start} and {end}: {result}")
        
        elif choice == '2':
            value = float(input("Enter the length value: "))
            direction = input("Enter 'M' for meters to feet or 'F' for feet to meters: ").strip().upper()
            result = length_converter(value, direction)
            if result is not None:
                print(f"Converted length: {result}")
            else:
                print("Invalid conversion direction.")
        
        elif choice == '3':
            text = input("Enter a text string: ")
            result = consonant_counter(text)
            print(f"Number of consonants: {result}")
        
        elif choice == '4':
            numbers = []
            count = int(input("How many numbers do you want to enter? "))
            for i in range(count):
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
            smallest, largest = min_max_finder(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")
        
        elif choice == '5':
            text = input("Enter a text string: ")
            result = palindrome_checker(text)
            print(f"Is palindrome: {result}")
        
        elif choice == '6':
            file_path = input("Enter the path to the text file: ")
            result = word_counter(file_path)
            if isinstance(result, dict):
                for word, count in result.items():
                    print(f"'{word}' occurs {count} times.")
            else:
                print(result)
        
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 7.")
        
        # Ask if the user wants to continue
        continue_choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()