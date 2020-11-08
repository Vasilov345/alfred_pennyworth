GREETINGS = ["Hi", "Hello", "Hola", "Privet"]


def generator_example():
    for greeting in GREETINGS:
        yield greeting
    yield "This is the last One"


def custom_generator():
    yield GREETINGS[0]
    yield GREETINGS[1]
    yield GREETINGS[2]
    yield GREETINGS[3]
    yield GREETINGS[4]


def check_generator_values(gen):
    try:
        while True:
            print(f"Next value from generator : {next(gen)}")
    except StopIteration:
        print("Thats all values we have in generator")


if __name__ == "__main__":
    greetings_gen = generator_example()

    check_generator_values(greetings_gen)

    generator_expression = (g for g in GREETINGS)
    check_generator_values(generator_expression)
