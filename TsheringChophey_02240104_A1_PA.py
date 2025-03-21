
def is_prime(num):
    """To check whether a number is prime or not."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_sum(start, end):
    """To calculate the sum of all prime numbers in a given range."""
    return sum(num for num in range(start, end + 1) if is_prime(num))


def length_converter(value, direction):
    """Conversion of length between meters and feet."""
    if direction == 'M':
        return round(value * 3.28084, 2)  # Meters to Feet
    elif direction == 'F':
        return round(value / 3.28084, 2)  # Feet to Meters
    else:
        return None


def consonant_count(text):
    """To count the number of consonants in a given string."""
    return sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou')


def min_max_finder(numbers):
    """To find the smallest and largest numbers in a list."""
    return min(numbers), max(numbers)


def is_palindrome(text):
    """To check if a string is a palindrome."""
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


    
    with open(file_path, 'r') as file:
        text = file.read().lower()    
        for word in words_to_count:
            counts[word] = text.count(word)
    
    return counts


def main():
    while True:
        print("\nMenu:")
        print("1. Calculating the sum of prime numbers")
        print("2. Length Unit Converter")
        print("3. Consonant Counter")
        print("4. Min-Max Number Finder")
        print("5. Palindrome Checker")
        print("6. Word Counter")
        print("7. Exit Program")

        choice = input("Select a function (1-7): ")

        if choice == '1':
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            result = prime_sum(start, end)
            print(f"Sum of prime numbers from {start} to {end} is: {result}")

        elif choice == '2':
            value = float(input("Enter length value: "))
            direction = input("Convert (M)eters to Feet or (F)eet to Meters? ").upper()
            result = length_converter(value, direction)
            if result is not None:
                print(f"Converted length: {result}")
            else:
                print("Invalid direction.")

        elif choice == '3':
            text = input("Enter a text string: ")
            result = consonant_count(text)
            print(f"Number of consonants: {result}")

        elif choice == '4':
            count = int(input("How many numbers do you want to enter? "))
            numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(count)]
            smallest, largest = min_max_finder(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")

        elif choice == '5':
            text = input("Enter a text string: ")
            result = is_palindrome(text)
            print(f"Is palindrome: {result}")

        elif choice == '6':
            def words_to_count(nameoffile):
                try:
                    with open(nameoffile,'r') as file:
                        content = file.read()
                except FileNotFoundError:
                    print("We Couldn't Find Your File!")
                    return{}

                words_needed_to_find = ["and", "the", "was"]
                words = content.lower().split()

                word_counts = {word: words.count(word) for word in words_needed_to_find}
                
                return word_counts

            nameoffile = input("Please enter the name of the file you want to count the word in: ").strip()

            counts = words_to_count(nameoffile)

            if counts: 
                for word, count in counts.items():
                    print(f"'{word}' appears {count} times.")
        exit_code = input("Wanna try again?(Yes/No): ").strip().upper()

        if choice == '7':
            print("Exiting the program. Thank You ")
            break



if __name__ == "__main__":
    main()