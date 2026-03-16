import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

class OpenAISample:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_response(self, messages):
        # Here you would typically use the OpenAI API to generate a response based on the prompt
        # For demonstration purposes, we'll return a mock response
        #return f"Generated response for prompt: '{prompt}' using API key: '{self.api_key}'"
        openAI = OpenAI(api_key=self.api_key)
        openAI_response = openAI.chat.completions.create(
            model="gpt-4.1-nano",  
            messages=messages)
        return openAI_response.choices[0].message.content
    
api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set your OpenAI API key in the environment variable
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment!")
if not api_key.startswith("sk-"):
    raise ValueError("Key doesn't look like a valid OpenAI key")

openAISample = OpenAISample(api_key)

message = "What is the capital of India?"
messages = [{"role": "user", "content": message}]

response = openAISample.generate_response(messages)
print(response)

#######################################################################################################
messages = [
    {"role": "system", "content": "You are a Political Analyst."},
    {"role": "user", "content": "What do you think about the current political situation in the World?"}
]

response = openAISample.generate_response(messages)
print(response)