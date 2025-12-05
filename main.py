import os
import argparse

from dotenv import load_dotenv # dotenv library is for storing confidential information in .env file that lives in the main direcotry
from google import genai
from google.genai import types

from prompts import SYSTEM_PROMPT
from call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description = "Agent AI") # Parser jest to biblioteka do obsługi user_inputów
    parser.add_argument("user_prompt", type = str, help = "User prompt") # type indicates required data type, help is a helpful note for the user if he run -h
    parser.add_argument("--verbose", action = "store_true", help = "Enable verbose output") # action - performs specific action Store_true return true is a flag is used and vice versa
    arguments = parser.parse_args()


    load_dotenv() # it looks for KEY=VALUE pairs in the .env file and for the later use, when en environment varaible is called
    my_api_key = os.environ.get("GEMINI_API_KEY") # the function creates a dictonaries with KEY-VALUE pair of the enviroment variables
    if not my_api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    
    client = genai.Client(api_key=my_api_key) # this is from the genai documentation on creating a client
    messages = [
        types.Content( # it contains multipule parts of content
            role = "user",
            parts = [types.Part(text = arguments.user_prompt)] # types.Part - datatype containing piece of content 
        )
    ]

    generate_content(client, messages, arguments.verbose)

def generate_content(client, messages, verbose):
    for i in range(20):
        try:
            print(f"Iterarion number {i}")    
            response = client.models.generate_content(# function makes an API call to the GEMINI model with a prompt provided under contents variable
                model = "gemini-2.5-flash",
                contents  = messages, # We are providing all the messages in the conversation to the Agent so that he has a history and context
                config = types.GenerateContentConfig(
                    system_instruction = SYSTEM_PROMPT, # set of instruction which tell the model how to behave
                    tools = [available_functions] # tools hold the code that enables the model to interact with external systems
                ),
            )


            for candidate in response.candidates:
                # print(f"Candidate.content is {candidate.content}\n")
                messages.append(candidate.content)

            # print(f"Updated messages: {messages}\n")

            if not response.usage_metadata:
                raise RuntimeError("Gemini API response appears to be malformed")

            if verbose:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

            # print(f"Response.function_calls is {response.function_calls}\n")
            function_call_list = []
            if response.function_calls:
                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose)
                    if not function_call_result.parts[0].function_response.response:
                        return "Error: Fatal Exception of some sorts"
                    function_call_list.append(function_call_result.parts[0])
                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
            

            # print(f"List of the functions responces {function_call_list}\n")
            # print(f"response.functions_calls are: {response.function_calls}, not responce.functions_call are {not response.function_calls}, responce.text is {response.text != None}\n")
            if not response.function_calls and response.text:
                print("Response:")
                print(response.text)
                break

            used_functions = types.Content(
                role = "user",
                parts = [types.Part(function_response = function_call_list[-1].function_response)]
            )

            # print(f"used_functions is {used_functions}\n")
            messages.append(used_functions)
            # print(f"The latest messages: {messages}\n")
            

        except:
            print("Error: error at iteration {i}")
            break

if __name__ == "__main__":
    main()
