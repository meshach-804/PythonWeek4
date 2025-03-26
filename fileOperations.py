import os

filename = input("Enter the name of the file to read: ")

try:
    # open the file for reading
    with open(filename, "r") as file:
        content = file.read()

    # Step 3: Modify the file content 
    modified_content = content.upper()

    # Step 4: Create a new file for the modified content
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write("Modified Content:\n")
        new_file.write(modified_content)
        new_file.write("\n\n[END OF FILE]")

    # Step 5: Confirm success to the user
    print(f"Success! Modified content has been written to {new_filename}.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist. Please check the name and try again.")
except PermissionError:
    print(f"Error: Permission denied to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")