import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    file_rel_path = os.path.join(working_directory, file_path)
    file_abs_path = os.path.abspath(file_rel_path)
    wd_abs_path = os.path.abspath(working_directory)
    # print(f"The joined relative dir is {file_rel_path}")
    # print(f"The joined absolute dir is {file_abs_path}")
    # print(f"The absolute working dir is {wd_abs_path}")

    if not file_abs_path.startswith(wd_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file_abs_path):
        return f'Error: File "{file_path}" not found.'
    
    if file_abs_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(
            ["python", file_rel_path, *args], 
            timeout = 30,
            capture_output = True,
            encoding = "UTF-8"
        )
        output = completed_process.stdout
        error = completed_process.stderr

        result = []
        if output:
            result.append(f"STDOUT:\n{output}")
        if error:
            result.append(f"STDERR:\n{error}")
        
        if completed_process.returncode != 0:
            result += f"\nProcess exited with code {completed_process.returncode}"

        return "/n".join(result) if result else f"No output produced"
    
    except Exception as e:
        return f"Error: executing Python file {e}"
    
# print(run_python_file("calculator", "main.py"))