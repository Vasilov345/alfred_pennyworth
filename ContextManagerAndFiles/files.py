import os


if __name__ == "__main__":

    with open("write_lines.txt", 'w') as f:
        f.writelines(["Hello, it`s me\n", "I was wondering if after all these years\n", ])

    with open("write.txt", 'w') as f:
        f.write("Some very wise text")

    with open("write_lines.txt", 'r') as f:
        result = f.read()
        print(f"What we have in write_lines.txt {result}")

    with open("write_lines.txt", 'r') as f:
        result = f.readlines()
        print(f"What we have in write_lines.txt {type(result)}: {result}")

    main_path = "dir_with_files"
    path = os.path.join(main_path, "write_lines.txt")

