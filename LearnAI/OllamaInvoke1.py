import os
import ollama
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

class OllamaSample:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_response(self, base_ul, messages):
        # Here you would typically use the OpenAI API to generate a response based on the prompt
        # For demonstration purposes, we'll return a mock response
        #return f"Generated response for prompt: '{prompt}' using API key: '{self.api_key}'"
        ollama = OpenAI(base_url=base_ul, api_key='ollama')
        openAI_response = ollama.chat.completions.create(
            model="llama3.2",  
            messages=messages)
        return openAI_response.choices[0].message.content
    

ollamaSample = OllamaSample("llama")

message = "What is the capital of India?"
messages = [{"role": "user", "content": message}]

OLLAMA_BASE_URL = "http://localhost:11434/v1"
response = ollamaSample.generate_response(OLLAMA_BASE_URL, messages)
print(response)

#######################################################################################################
messages = [
    {"role": "user", "content": "Tell me a fun fact"}
]

response = ollamaSample.generate_response(OLLAMA_BASE_URL, messages)
print(response)