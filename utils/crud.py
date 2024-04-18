
def read(users: list[dict]) ->None:
    for user in users[1:]:
        print(f"Twój znajomy {user['name']} opublikował: {user['posts']}")


def search(users: list[dict]) -> None:
    for user in users[1:]:
        user_name: str = input("Kogo szukasz: ")
        if user["name"] == user_name:
            print(users)
