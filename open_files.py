
def run():
    """ these functions execute open_this_file() function with file_name as parameter """
    print("Open a file")
    file_name = input("Enter file name: ")
    open_this_file(file_name)
    print("end program...")


def open_this_file(file_name):
    with open(f'files/{file_name}', mode='r', encoding='utf-8') as file:
        for dato in file:
            print(file.read())


def write():
    names = ['Alejandro', 'Edgar', 'Nieves', 'Diego', 'Karína']

    with open('./files/names.txt', 'w', encoding='utf-8') as file:
        for name in names:
            file.write(name)
            file.write('\n')

def read():
    numbers = []
    with open('./files/test.txt', 'r', encoding='utf-8') as file:
        for number in file:
            numbers.append(int(number))

    return numbers


def add_data():
    newUser = 'Antuan'
    with open('./files/names.txt', 'a', encoding='utf-8') as file:
        file.write(newUser)


if __name__ == '__main__':
    add_data()
