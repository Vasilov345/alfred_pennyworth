from abc import abstractmethod, ABC


# Not fully abstract class
class Greetings:

    @abstractmethod
    def say_hello(self):
        raise NotImplementedError


class English(Greetings):

    def say_hello(self):
        print("Hello!")


class Ukraine(Greetings):
    def say_hello(self):
        print("Доброго дня!")


# Fully abstract
class GreetingsAbstract(ABC):

    @abstractmethod
    def say_hello(self):
        raise NotImplementedError


class Greece(GreetingsAbstract):
    pass


class Spain(GreetingsAbstract):

    def say_hello(self):
        print("Hola!")


if __name__ == "__main__":
    fred = Greetings()
    try:
        fred.say_hello()
    except NotImplementedError as e:
        print(f"Method not exist. {e}")

    john = English()
    john.say_hello()

    vasya = Ukraine()
    vasya.say_hello()

    konchita = Spain()
    konchita.say_hello()

    # Python Will not create instance of abstract class
    try:
        abstract_fred = GreetingsAbstract()
    except TypeError as e:
        print(e)

    # All abstract methods should be implemented
    try:
        dionis = Greece()
    except Exception as e:
        print(e)
