# Decorators expect to receive a function as an argument,
# that is why we have to build a function that takes those extra arguments and generate our decorator on the fly.

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name="p"):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))

        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    return "Hello " + name

# 1. call tags("p") -> return tags_decorator

# 2. call get_text = tags_decorator(get_text) -> return func_wrapper
# 3. if call get_text -> func_wrapper(name)

print(get_text("John"))  # Outputs <p>Hello John</p>
