def write_to_file():
    try:
        # Open file in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("Line 1: It is sunny today.\n")
            file.write("Line 2: 12345\n")
            file.write("Line 3: Kenya is a beautiful country.\n")
        print("File 'my_file.txt' created and initial content written successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File write operation completed.")


def read_and_display_file():
    try:
        # Open file in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("\nContents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File read operation completed.")


def append_to_file():
    try:
        # Open file in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three more lines of text to the file
            file.write("\nLine 4: Appended line 1.\n")
            file.write("Line 5: 67890\n")
            file.write("Line 6: Life in kenya is beautiful.\n")
        print("\nAdditional content appended to 'my_file.txt' successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File append operation completed.")


# Main function
def main():
    write_to_file()
    read_and_display_file()
    append_to_file()


if __name__ == "__main__":
    main()
