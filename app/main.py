class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        pers = Person(person["name"], person["age"])
        person_list.append(pers)
    for person in people:
        pers = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            pers.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            pers.husband = Person.people[person["husband"]]
    return person_list
