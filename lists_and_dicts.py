

def run():
    my_list = ["Hola", True, 10]
    my_dict = {"name": "Alejandro", "position": "python developer"}

    # lista que contiene diccionarios
    super_list = [
        {
            "name": "Alejandro",
            "position": "python developer",
            "email": "acruz@breakfood.com"
        },
        {
            "name": "Edgar",
            "position": "fron-end developer",
            "email": "efranco@breakfood.com"
        }
    ]

    for user in super_list:
        print('_*' * 10)
        print(user["name"])
        print(user["position"])
        print(user["email"])


    # diccionario que contiene listas
    super_dict = {
        "UserUno": ["Alejandro", True, 24],
        "UserDos": ["Edgar", False, 23],
        "UserTres": ["Karina", False, 26]
    }

    for key, value in super_dict.items():
        print('_*' * 10)
        print(key)
        print(value)

if __name__ == '__main__':
    run()