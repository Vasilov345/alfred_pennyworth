import json

programmer = {"name": "denys", "stack": ["Python", "TDD"], "age": 27}

# dumps
json_dumps = json.dumps(programmer)
print(f"Json dumps type: {type(json_dumps)} value : {json_dumps}")

# loads
new_programmer = json.loads(json_dumps)
print(f"Json loads type: {type(new_programmer)} value : {new_programmer}")

# dump
with open("json_example.json", "w") as file:
    json.dump(programmer, file)

# load
with open("json_example.json", "r") as file:
    print(f"Loaded value from file {json.load(file)}")
