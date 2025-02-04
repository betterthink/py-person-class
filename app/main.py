class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person(human["name"], human["age"])
    for human in people:
        person = Person.people[human["name"]]
        if "wife" in human and human["wife"]:
            person.wife = Person.people[human["wife"]]
        if "husband" in human and human["husband"]:
            person.husband = Person.people[human["husband"]]
    return list(Person.people.values())


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
