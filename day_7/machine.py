from elf_machine import ElfMachine


class Day7(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        # build file tree structure using commands
        commands = input_data.split("$ ")
        current_dir = ""
        file_tree = {}
        directory_tree = {}
        for line in commands:
            cmd = line.split("\n")[0]
            output = line.split("\n")[1:]

            match cmd.split(" "):
                case "cd", dir_name:
                    if dir_name == "..":
                        if current_dir.count("/") == 1:
                            current_dir = "/"
                        else:
                            split_index = current_dir.rfind("/")
                            current_dir = current_dir[:split_index]
                    elif dir_name == "/":
                        current_dir = dir_name
                    else:
                        if current_dir == "/":
                            current_dir = f"{current_dir}{dir_name}"
                        else:
                            current_dir = f"{current_dir}/{dir_name}"

                    if not file_tree.get(current_dir):
                        file_tree[current_dir] = {}
                    if not directory_tree.get(current_dir):
                        directory_tree[current_dir] = []

                case ["ls"]:
                    for file in output:
                        if file.startswith("dir"):
                            dir_name = file.split(" ")[1]
                            if current_dir == "/":
                                directory_tree[current_dir].append(
                                    f"{current_dir}{dir_name}"
                                )
                            else:
                                directory_tree[current_dir].append(
                                    f"{current_dir}/{dir_name}"
                                )
                            continue
                        if file == "":
                            continue
                        size, filename = file.split(" ")
                        file_tree[current_dir][filename] = int(size)
                case _:
                    continue

        # calculate directory sizes (files only)
        directory_sizes_files_only = {}
        for directory, files in file_tree.items():
            directory_sizes_files_only[directory] = sum(files.values())

        max_directory_sum = 0
        directory_sizes = {}

        # calculate directory sizes (with subdirectories)
        for directory in directory_tree.keys():
            size = 0

            def _get_size(dir_name):
                if directory_tree[dir_name]:
                    size = directory_sizes_files_only[dir_name]
                    for subdir in directory_tree[dir_name]:
                        size += _get_size(subdir)

                    return size

                else:
                    return directory_sizes_files_only[dir_name]

            size += _get_size(directory)

            directory_sizes[directory] = size

        for size in directory_sizes.values():
            if size <= 100000:
                max_directory_sum += size

        return max_directory_sum

    def solve_second_puzzle(self, input_data: str) -> str:
        # build file tree structure using commands
        commands = input_data.split("$ ")
        current_dir = ""
        file_tree = {}
        directory_tree = {}
        for line in commands:
            cmd = line.split("\n")[0]
            output = line.split("\n")[1:]

            match cmd.split(" "):
                case "cd", dir_name:
                    if dir_name == "..":
                        if current_dir.count("/") == 1:
                            current_dir = "/"
                        else:
                            split_index = current_dir.rfind("/")
                            current_dir = current_dir[:split_index]
                    elif dir_name == "/":
                        current_dir = dir_name
                    else:
                        if current_dir == "/":
                            current_dir = f"{current_dir}{dir_name}"
                        else:
                            current_dir = f"{current_dir}/{dir_name}"

                    if not file_tree.get(current_dir):
                        file_tree[current_dir] = {}
                    if not directory_tree.get(current_dir):
                        directory_tree[current_dir] = []

                case ["ls"]:
                    for file in output:
                        if file.startswith("dir"):
                            dir_name = file.split(" ")[1]
                            if current_dir == "/":
                                directory_tree[current_dir].append(
                                    f"{current_dir}{dir_name}"
                                )
                            else:
                                directory_tree[current_dir].append(
                                    f"{current_dir}/{dir_name}"
                                )
                            continue
                        if file == "":
                            continue
                        size, filename = file.split(" ")
                        file_tree[current_dir][filename] = int(size)
                case _:
                    continue

        # calculate directory sizes (files only)
        directory_sizes_files_only = {}
        for directory, files in file_tree.items():
            directory_sizes_files_only[directory] = sum(files.values())

        max_directory_sum = 0
        directory_sizes = {}

        # calculate directory sizes (with subdirectories)
        for directory in directory_tree.keys():
            size = 0

            def _get_size(dir_name):
                if directory_tree[dir_name]:
                    size = directory_sizes_files_only[dir_name]
                    for subdir in directory_tree[dir_name]:
                        size += _get_size(subdir)

                    return size

                else:
                    return directory_sizes_files_only[dir_name]

            size += _get_size(directory)

            directory_sizes[directory] = size

        for size in directory_sizes.values():
            if size <= 100000:
                max_directory_sum += size

        unused_space = 70000000 - directory_sizes["/"]
        space_required = 30000000 - unused_space

        smallest = None
        for dir_size in directory_sizes.values():
            if dir_size >= space_required:
                if not smallest or dir_size < smallest:
                    smallest = dir_size

        return smallest
