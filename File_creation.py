import os

def create_file():
    folder_name = input("Enter the folder name: ").strip()

    # Create the folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)

    try:
        num_files = int(input("Enter the number of files: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    extension = input("Enter the file extension (e.g., txt, py): ").strip().lstrip(".")

    for i in range(1, num_files + 1):
        file_name = f"Q{i}.{extension}"
        file_path = os.path.join(folder_name, file_name)

        with open(file_path, "w") as f:
            f.write(f"#This is {file_name} in the '{folder_name}' folder.\n")

    print(f"\n✅ Folder '{folder_name}' created successfully.")
    print(f"✅ {num_files} '.{extension}' files created.")

if __name__ == "__main__":
    create_file()