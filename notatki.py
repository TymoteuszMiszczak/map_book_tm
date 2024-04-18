users: list[dict] = [
{"name": "Tymoteusz", "surname": "Miszczak", "posts": 21},
    {"name": "Maciej", "surname": "Przybytek", "posts": 45},
    {"name": "Bartosz", "surname": "Pietrasik", "posts": 60},
    {"name": "Janek", "surname": "Mielec", "posts": 20},
    {"name": "Mateusz", "surname": "Matysiak", "posts": 33},
]


def create_user(users:list[dict])->None:
    name: str = input("Podaj imię użytkownika: ")
    surname: str = input("Podaj nazwisko użytkownika: ")
    posts: str = int(input("Podaj liczbę postów: "))
    user: dict = {"name": name, "surname": surname, "posts": posts}
    users.append(user)

create_user(users)

print(users)