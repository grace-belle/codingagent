import os

def get_files_info(working_directory, directory="."):
    selected_directory = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(selected_directory, directory))
    valid_target_directory = os.path.commonpath([selected_directory, target_directory]) == selected_directory
    try:
        if not valid_target_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" does not exist'  
        lines = []
        for filename in os.listdir(target_directory):
                filepath = os.path.join(target_directory, filename)
                stat_result = os.stat(filepath)
                lines.append(f'- {filename}: file_size={stat_result.st_size} bytes, is_dir={os.path.isdir(filepath)}')
        return "\n".join(lines)
    except Exception as e:
        return f'Error: {str(e)}'