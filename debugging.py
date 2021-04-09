
# def divisors(number):
#     return [i for i in range(1, number + 1) if number % i == 1]

divisors = lambda  number: [i for i in range(1, number + 1) if number % i == 0]


def run():
    try:
        number = int(input("Type a number: "))

        if number <= 0:
            raise TypeError("Please enter a positive number")

    except ValueError:
        print("Please enter a number, strings not allowed")
    except TypeError as TE:
        print(TE)
    else:
        print(divisors(number))
    finally:
        print("End program...")


if __name__ == '__main__':
    run()