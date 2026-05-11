import os
from dotenv import load_dotenv
import requests

load_dotenv(override=True)

from openai import OpenAI

class OpenRouterSample:
    def __init__(self, api_key):
        self.api_key = api_key  
    
    def generate_response(self, base_ul, messages):
        # Here you would typically use the OpenAI API to generate a response based on the prompt
        # For demonstration purposes, we'll return a mock response
        # return f"Generated response for prompt: '{prompt}' using API key: '{self.api_key}'"
        openRouter = OpenAI(base_url=base_ul, api_key=self.api_key)
        response = openRouter.chat.completions.create(
            model="x-ai/grok-4.3",  
            messages=messages)
        return response.choices[0].message.content

openrouter_api_key = os.getenv('OPENROUTER_API_KEY')    
if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment!")
else:
    print("OpenRouter API key is valid and found in environment.")
openRouterSample = OpenRouterSample(openrouter_api_key)

message = "Tell me a fun fact about the Indian Railways?"
messages = [{"role": "user", "content": message}]   

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
response = openRouterSample.generate_response(OPENROUTER_BASE_URL, messages)    
print(response)