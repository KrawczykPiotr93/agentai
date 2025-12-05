from google.genai import types
from functions.schemas import *
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file 

available_functions = types.Tool(
    function_declarations = [
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

function_mapping = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file
}

def call_function(function_call_part, verbose = False):
    function_name = function_call_part.name
    keyword_arguments = function_call_part.args

    if verbose:
        print(f"Calling function: {function_name}({keyword_arguments})")
    else:
        print(f" - Calling function: {function_name}")
    
    keyword_arguments.update({"working_directory": "./calculator"})
    
    if function_name not in function_mapping:
        return types.Content(
            role = "tool",
            parts = [
                types.Part.from_function_response(
                    name = function_name,
                    response = {"Error": f"Unknown function: {function_name}"},
                )
            ],
        )

    function_result = function_mapping[function_name](**keyword_arguments)

    return types.Content(
        role = "tool",
        parts = [
            types.Part.from_function_response(
                name = function_name,
                response = {"result": function_result},
            )
        ],
    )
