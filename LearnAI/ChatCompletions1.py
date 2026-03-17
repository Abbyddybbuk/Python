import os
from dotenv import load_dotenv
import requests

load_dotenv(override=True)

from openai import OpenAI

class ChatCompletions1:
    def __init__(self, api_key):
        self.api_key = api_key

    def post_request(self, url, headers, payload):
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
    
api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set your OpenAI API key in the environment variable
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment!")
if not api_key.startswith("sk-"):
    raise ValueError("Key doesn't look like a valid OpenAI key")
else:
    print("API key is valid and found in environment.")

chatCompletions1 = ChatCompletions1(api_key)

headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
payload = {"model": "gpt-4.1-nano", "messages": [{"role": "user", "content": "Tell me a fun fact about the United Kingdom"}]  }
url="https://api.openai.com/v1/chat/completions"

response = chatCompletions1.post_request(url, headers, payload)
print(response)

