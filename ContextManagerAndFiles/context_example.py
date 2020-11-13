class ContextManager:

    def __enter__(self):
        print("Before")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("After")
        print(f"We catch exception {exc_type}")
        pass

    def do_something(self):
        print("Something important")

try:
    print("Before")
    obj = ContextManager()
    obj.do_something()
except Exception as e:
    print("We catch Exception")
finally:
    print("After")



with ContextManager() as obj: # <-- Before
    obj.do_something()
    raise TypeError # <=== Your logic
    pass
# After

print("Something after our logic")