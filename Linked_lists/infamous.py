def collatz_sequence(number):
    while number != 0:
        if number % 2 == 1:  # Number is odd
            number = number * 3 + 1
        else:  # Number is even
            number = number // 2
        print(number)

if __name__ == "__main__":
    try:
        input_number = int(input("Enter a number: "))
        collatz_sequence(input_number)
    except ValueError:
        print("Please enter a valid integer.")
