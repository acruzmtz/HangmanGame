# practicing assert statements

divisors = lambda  number: [i for i in range(1, number + 1) if number % i == 0]

def run():
    try:
        number = input("Type a number: ")
        assert number.isdigit(), "Please enter a positive number, strings not allowed"
        assert int(number) > 0, "The number must be greater than zero"

    except AssertionError as e:
        print("Error: ", e)
    else:
        print(divisors(int(number)))
    finally:
        print("End program...")


if __name__ == '__main__':
    run()