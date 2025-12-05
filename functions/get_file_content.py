import os
from functions.config import MAX_CHARACTERS

def get_file_content(working_directory, file_path):
    file_rel_path = os.path.join(working_directory, file_path)
    file_abs_path = os.path.abspath(file_rel_path)
    wd_abs_path = os.path.abspath(working_directory)
    # print(f"The joined relative dir is {file_rel_path}")
    # print(f"The joined absolute dir is {file_abs_path}")
    # print(f"The absolute working dir is {wd_abs_path}")

    if not file_abs_path.startswith(wd_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file_abs_path, "r") as f:
            file_content_string = f.read()
        if len(file_content_string) >= MAX_CHARACTERS:
            file_content_string = file_content_string[:MAX_CHARACTERS] + f"\n...File \"{file_path}\" truncated at 10000 characters]"
        return file_content_string
    
    except Exception as e:
        f"Error retriving a file: {e}"



