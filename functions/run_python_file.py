import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

        if not abs_file_path.startswith(abs_working_dir):
            raise ValueError(f"Cannot execute \"{file_path}\" as it is outside the permitted working directory")
        if not os.path.isfile(abs_file_path):
            raise ValueError(f"\"{file_path}\" does not exist")
        if not abs_file_path.endswith('.py'):
            raise ValueError(f"\"{file_path}\" is not a Python file")
        command = ["python", abs_file_path]
        if args:
            command.extend(args)
        try:
            process = subprocess.run(command, capture_output=True, text=True, timeout=30)
            output = []
            if process.returncode != 0:
                output.append(f"Process exited with code {process.returncode}")
            if not process.stdout and not process.stderr:
                output.append("No output produced")
            if process.stdout:
                output.append(f"STDOUT:\n{process.stdout}")
            if process.stderr:
                output.append(f"STDERR:\n{process.stderr}")
            return "\n".join(output)
        except Exception as e:
            return f"Error executing the file: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the specified working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING)
            ),
        },
    ),
)