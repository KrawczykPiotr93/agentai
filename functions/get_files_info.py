import os

def get_files_info(working_directory, directory="."):

    dir_rel_path = os.path.join(working_directory, directory)
    dir_abs_path = os.path.abspath(dir_rel_path)
    wd_abs_path = os.path.abspath(working_directory)
    # print(f"The joined relative dir is {dir_rel_path}")
    # print(f"The joined absolute dir is {dir_abs_path}")
    # print(f"The absolute working dir is {wd_abs_path}")

    if not dir_abs_path.startswith(wd_abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(dir_abs_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_contents = os.listdir(dir_abs_path)
        contents_list = ''
        for item in dir_contents:
            item_dir = os.path.join(dir_abs_path, item)
            contents_list += f"- {item}: file_size={os.path.getsize(item_dir)}, is_dir={os.path.isdir(item_dir)}\n"
        return contents_list
    except Exception as e:
        return f"Error listing files: {e}"
    


