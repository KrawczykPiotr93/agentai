from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name = "get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "directory": types.Schema(
                type = types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name = "get_file_content",
    description="Lists content of a file at specified path, constrained to the working directory. Truncates files longer than 10000 characters",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "Required property. It's a path of a file relative to the working directory",
            ),
        },
    required = ["file_path"]    
    ),
)

schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description="writes specified content to a file at specified path, constrained to the working directory",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "Required property. It's a path of a file relative to the working directory",
            ),
            "content": types.Schema(
                type = types.Type.STRING,
                description = "Required property. Specified what text to add to the file",
            )
        },
    required = ["file_path", "content"]    
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name = "run_python_file",
    description="Executes program at a specified path, constrained to the working directory.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "Required property. It's a path of a file relative to the working directory",
            ),
            "args": types.Schema(
                type = types.Type.ARRAY,
                items = types.Schema(
                type = types.Type.STRING,
                description = "Lists arguments that should be passed to a executed script",
            ),
            description = "Lists arguments that should be passed to a executed script",
            ),
        },
    required = ["file_path"]    
    ),
)