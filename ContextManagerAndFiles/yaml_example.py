import yaml

programmer = {"name": "denys", "stack": ["Python", "TDD"], "age": 27}

# dump
with open("yaml_file.yml", "w") as file:
    yaml.dump(programmer, file)

# load
with open("yaml_file.yml", "r") as file:
    print(f"Loaded value from file {yaml.load(file, Loader=yaml.FullLoader)}")
