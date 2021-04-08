# en python solo se permite que sea de una linea

USERS = []

def run(name, age):
    USERS.append(name)
    USERS.append(age)

    print(USERS)


if __name__ == '__main__':
    print("Ejemplo de usar una función lambda")

    name = input('Nombre: ')
    age = int(input('Edad: '))

    # usando funciones normales
    #run(name, age)

    # usando lambda functions
    users = lambda name, age: USERS.append(name); USERS.append(age)
    users(name, age)
    print(USERS)