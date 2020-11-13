import datetime
import json


class ObjectWithSimpleAttributes:

    def __init__(self, some_string: str, some_list: list, some_dict: dict, some_int: int):
        self.some_string = some_string
        self.some_list = some_list
        self.some_dict = some_dict
        self.some_int = some_int


class Person:

    def __init__(self, name: str, dob: datetime.datetime):
        self.name = name
        self.dob = dob

    def default(self):
        return self.__dict__


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectWithSimpleAttributes):
            return obj.__dict__

        # if isinstance(obj, Person):
        #     return obj.__dict__

        # if isinstance(obj, datetime.datetime):
        #     return obj.isoformat()

        return json.JSONEncoder.default(self, obj)


if __name__ == "__main__":
    # object with simple attributes
    simple_obj = ObjectWithSimpleAttributes(
        some_string="Hey",
        some_list=["Hey ho", 12],
        some_int=888,
        some_dict={"hey": 78}
    )
    print(f"simple_obj: {json.dumps(simple_obj, cls=Encoder)}")

    person = Person("Den", datetime.datetime(day=4, month=9, year=2020))
    print(json.dumps(person, cls=Encoder))
