if __name__ == "__main__":
    n = int(input())
    holly_list, list_args = [], []

    def exec_command(command: str, *args: int):
        for _ in args:
            list_args.append(int(_))
        if command == "insert":
            holly_list.insert(*list_args)
        elif command == "print":
            print(holly_list)
        elif command == "remove":
            holly_list.remove(*list_args)
        elif command == "append":
            holly_list.append(*list_args)
        elif command == "sort":
            holly_list.sort()
        elif command == "pop":
            holly_list.pop()
        elif command == "reverse":
            holly_list.reverse()
        else:
            exit()
        list_args.clear()

    for _ in range(n):
        exec_command(*input().split(" "))
