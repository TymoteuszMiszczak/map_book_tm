users: list[dict] = [
{"name": "Tymoteusz", "surname": "Miszczak", "posts": 21},
    {"name": "Maciej", "surname": "Przybytek", "posts": 45},
    {"name": "Bartosz", "surname": "Pietrasik", "posts": 60},
    {"name": "Janek", "surname": "Mielec", "posts": 20},
    {"name": "Paweł", "surname": "Paszkowski", "posts": 1},
    {"name": "Mateusz", "surname": "Matysiak", "posts": 33},
]
def remove(users:list[dict]) ->None:
    for user in users[1:]:
        menu_option: str = input("Kogo szukasz: ")
        if user ["name"]==user_name:
            users.remove(users)


remove(users)
print(users)


