import os
import openai
from config import apikey

openai.api_key = apikey

prompt = ""


def change_prompt(text):
    global prompt
    prompt = text
    # print("Inside the function")
    # print(prompt)
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{prompt}",
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # print(response);
        return response
    except Exception as e:
        print(e)
