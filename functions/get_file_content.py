import os

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

        if not abs_file_path.startswith(abs_working_dir):
            raise ValueError(f"Error: Cannot read {file_path} as it is outside the working directory.")
        if not os.path.isfile(abs_file_path):
            raise ValueError(f"Error: {file_path} is not a file.")
        with open(abs_file_path, 'r') as file:
            content = file.read(MAX_CHARS)
            if file.read(1) != '':
                return content[:MAX_CHARS] + "\n\n[Content truncated due to length]"
        return content
    except Exception as e:
        return str(e)