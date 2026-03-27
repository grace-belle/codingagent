import os

def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

        if not abs_file_path.startswith(abs_working_dir):
            raise ValueError(f"Error: Cannot write to {file_path} as it is outside the permitted working directory")
        if os.path.isdir(abs_file_path):
            raise ValueError(f"Error: {file_path} is a directory, cannot write to it.")
        with open(abs_file_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return str(e)