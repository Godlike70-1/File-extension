import os

def change_file_extension(file_path, new_extension):
    try:
        # Extract the directory, filename, and current extension
        base = os.path.splitext(file_path)[0]
        new_file = f"{base}.{new_extension}"

        # Rename the file
        os.rename(file_path, new_file)
        print(f"File extension changed successfully: {new_file}")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("File Extension Changer")
    file_path = input("Enter the full path of the file (e.g., C:\\path\\to\\file.txt): ").strip()
    new_extension = input("Enter the new extension (without the dot, e.g., 'jpg'): ").strip()

    if not new_extension:
        print("Error: No extension provided.")
    else:
        change_file_extension(file_path, new_extension)