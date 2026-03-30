import os
import argparse
from prompts import system_prompt
from dotenv import load_dotenv
from call_function import available_functions, call_function
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
	raise RuntimeError("no api key")
client = genai.Client(api_key=api_key)

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = client.models.generate_content(
	model="gemini-2.5-flash",
	contents=messages, config=types.GenerateContentConfig(tools = [available_functions], system_instruction=system_prompt))
    usage = response.usage_metadata

    if args.verbose:
        print("User prompt: ", args.user_prompt)
        print("Prompt tokens: ", usage.prompt_token_count)
        print("Response tokens: ", usage.candidates_token_count)
    
    if response.function_calls:
        function_responses = []
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=args.verbose)
            if not function_call_result.parts:
                raise RuntimeError(f"Function call result has no parts: {function_call_result}")
            if not function_call_result.parts[0].function_response:
                raise RuntimeError(f"Function call result part has no function response: {function_call_result.parts[0]}")
            if not function_call_result.parts[0].function_response.response:
                raise RuntimeError(f"Function call result part has no function response content: {function_call_result.parts[0].function_response}")
            function_responses.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")      
    
             
    else:
        print(response.text)
        
    
if __name__ == "__main__":
    main()
