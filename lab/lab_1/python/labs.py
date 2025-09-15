import os


def test_file_with_content():
    print("Test 1: File with content")
    try:
        with open("lab.txt", "w") as writer:
            writer.write("Hello World\nSecond Line")

        print("Expected: Hello World Second Line")
        print("Actual: ", end="")

        with open("lab.txt", "r") as reader:
            content = reader.read()

            if not content:
                print("The file is empty.")
            else:
                print(content.replace("\n", " "), end="")

        os.remove("lab.txt")

    except Exception as e:
        print(f"Test failed: {e}")
    print("\n")


def test_empty_file():
    print("Test 2: Empty file")
    try:
        open("test2.txt", "w").close()

        print("Expected: The file is empty.")
        print("Actual: ", end="")

        with open("test2.txt", "r") as reader:
            content = reader.read()

            if not content:
                print("The file is empty.")
            else:
                print(content, end="")

        os.remove("test2.txt")

    except Exception as e:
        print(f"Test failed: {e}")
    print()


def test_file_not_found():
    print("Test 3: File not found")
    try:
        print("Expected: FileNotFoundError")
        print("Actual: ", end="")

        with open("nonexistent.txt", "r") as reader:
            pass

    except FileNotFoundError:
        print("FileNotFoundError (PASS)")
    except Exception as e:
        print(f"Wrong exception: {e}")
    print()


def run_tests():
    print("Running TextFileReader Tests...\n")

    test_file_with_content()
    test_empty_file()
    test_file_not_found()

    print("All tests completed!")


if __name__ == "__main__":
    run_tests()
