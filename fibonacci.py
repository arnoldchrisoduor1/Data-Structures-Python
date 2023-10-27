def fibonacci_upto(limit):
    sequence = [0, 1]
    while True:
        next_number = sequence[-1] + sequence[-2]
        if next_number <= limit:
            sequence.append(next_number)
        else:
            break
    return sequence

limit = int(input("Give the limit of the fibonacci sequence: "))
fib_numbers = fibonacci_upto(limit)
print(f"The fibonacci sequence upto, {limit}, are {fib_numbers}")