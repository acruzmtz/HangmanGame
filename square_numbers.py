import math

def example():
    """
    examples of list comprehension and dictionary comprehension
    """
    square_numbers = [i ** 2 for i in range(1, 101) if i % 3 != 0]

    square_numbers_with_dict = {f"{i}": i ** 2 for i in range(1, 101) if i % 3 != 0}

    print(square_numbers_with_dict)


def run():
    """create a list comprehension that save numbers in range 1 to 10000

    Returns:
        list: numbers divisible by 4, 6 and 9 
    """
    return [number for number in range(1, 10000) if number % 4 == 0 if number % 6 == 0 if number % 9 == 0]


def get_the_first_thousand_numbers():
    return {number: math.sqrt(number) for number in range(1, 1001)}


if __name__ == '__main__':
    numbers = get_the_first_thousand_numbers()
    print(numbers)