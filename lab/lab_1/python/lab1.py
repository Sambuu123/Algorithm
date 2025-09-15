def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

            if not content:
                print("The file is empty.")
            else:
                print(content, end='')

    except FileNotFoundError:
        print(f"Error: File not found : {filename}")
    except IOError as e:
        print(f"Error reading file: {e}")


def main():
    filename = input("Enter filename: ")
    read_file(filename)


if __name__ == "__main__":
    main()
