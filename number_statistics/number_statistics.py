def main():
    numbers = []
    while True:
        number = int(input("Enter a number: "))
        numbers.append(number)

        again = input("Continue? (y/n): ")
        if again == "n":
            break
        elif again not in ["y", "n"]:
            print("Please enter y or n")
    print(f"Numbers entered: {len(numbers)}")
    print(f"Numbers: {numbers}")
    print(f"Largest: {largest_number(numbers)}")
    print(f"Smallest: {smallest_number(numbers)}")
    print(f"Sum: {total_sum(numbers)}")
    print(f"Average: {average_number(numbers):.2f}")


def total_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


def largest_number(numbers):
    largest = numbers[0]
    for x in numbers:
        if x > largest:
            largest = x
    return largest


def smallest_number(numbers):
    smallest = numbers[0]
    for x in numbers:
        if x < smallest:
            smallest = x
    return smallest


def average_number(numbers):
    average = total_sum(numbers) / len(numbers)
    return average


main()
