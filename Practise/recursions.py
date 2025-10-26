import os

def search_file(directory, target_file):
    """
    Recursively search for a file inside all subdirectories.
    """
    print(f"Searching in: {directory}")
    
    try:
        for item in os.listdir(directory):
            path = os.path.join(directory, item)

            # If file matches, return the full path
            if item == target_file:
                return f"File found: {path}"

            # If it's a folder, search inside it (recursive call)
            if os.path.isdir(path):
                result = search_file(path, target_file)
                if result:
                    return result
    except PermissionError:
        # Skip folders without access
        pass

    return None

# Example usage
directory_path = "C:/Users"
file_to_find = "example.txt"

result = search_file(directory_path, file_to_find)
if result:
    print(result)
else:
    print("File not found.")
