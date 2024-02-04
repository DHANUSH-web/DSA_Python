class Person:

    def __init__(self, name: str, age: int, userId: str) -> None:
        self.name = name
        self.age = age
        self.userId = userId.encode()

    def get_user_id(self) -> str:
        return self.userId.decode()
