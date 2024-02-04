from person import Person
import numpy as np
import string


def generate_user_id() -> str:
    pattern = string.ascii_letters + string.digits
    return "".join(np.random.choice(list(pattern), size=20))


DATABASE_SIZE = 2000

users = np.array([
        dict(name=f"user_#{i+1}", age=np.random.randint(20, 30), userId=generate_user_id())
        for i in range(DATABASE_SIZE)
    ])
user_objects: list[Person] = []

for user in users:
    person = Person(name=user['name'], age=user['age'], userId=user['userId'])
    user_objects.append(person)

for person in user_objects:
    print(f"Name: {person.name}, Age: {person.age}, UserId: {person.get_user_id()}")
