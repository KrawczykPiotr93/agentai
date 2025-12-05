import os

def write_file(working_directory, file_path, content):
    rel_file_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(rel_file_path)
    abs_wd_path = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_wd_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(abs_wd_path):
            os.makedirs(abs_wd_path)
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error writing file {e}"
    


