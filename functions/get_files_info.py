def get_files_info(working_directory, directory="."):
    selected_directory = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(selected_directory, directory))
    valid_target_directory = os.path.commonpath([selected_directory, target_directory]) == selected_directory
    if not valid_target_directory:
        return {f'Error: Cannot list "{directory}" as it is outside the permitted working directory'}
    if not directory_exists(directory):
        return {f'Error: "{directory}" does not exist'}