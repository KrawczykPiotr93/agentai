import os
import sys
from dotenv import load_dotenv # dotenv library is for storing confidential information in .env file that lives in the main direcotry
from google import genai
from google.genai import types
from prompts import SYSTEM_PROMPT
from functions.schemas import schema_get_files_info

def main():
    load_dotenv() # it looks for KEY=VALUE pairs in the .env file and for the later use, when en environment varaible is called
    my_api_key = os.environ.get("GEMINI_API_KEY") # the function creates a dictonaries with KEY-VALUE pair of the enviroment variables
    client = genai.Client(api_key=my_api_key) # this is from the genai documentation on creating a client

    available_functions = types.Tool(
        function_declarations = [
            schema_get_files_info
        ],
    )

    if len(sys.argv) == 1:
        print("Agent AI here")
        print("Please run the command with a prompt.")
        print("Example prompt: uv run main py \"What is going on?\"")
        sys.exit(1)

    
    arguments = sys.argv[1:]
    user_prompt = (" ").join(arguments)
    verbose = "--verbose" in arguments
    # print(f"The user prompt is: {user_prompt}")

    messages = [
        types.Content( # it contains multipule parts of content
            role = "user",
            parts = [types.Part(text = user_prompt)] # types.Part - datatype containing piece of content 
        )
    ]

    response = client.models.generate_content( # function makes an API call to the GEMINI model with a prompt provided under contents variable
        model = "gemini-2.0-flash-001",
        contents = messages, # We are prociding all the messages in the conversation to the Agent so that he has a history and context
        config = types.GenerateContentConfig( # optional configuration parameters
            system_instruction = SYSTEM_PROMPT, # set of instruction which tell the model how to behave
            tools = [available_functions] # tools hold the code that enables the model to interact with external systems
        ),
    )

    if verbose:
        print(f"User prompt: {user_prompt}" )
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print("Response:")
        print(response.text)
        # print(f"Messages are: {messages}")

if __name__ == "__main__":
    main()
