#!/usr/bin/env python3

"""
A quick and dirty Python script to ask GPT-3 for a prompt and print the response.
"""

import os
import openai
import time

SYSTEM_MESSAGE = """
Provide short, concise answers to the user's questions.
"""


def main():
    # input user
    user_input = input("You : ")
    
    # histori yang ditanyakan sebelumnya
    chat_history = []

    # perulangan komunikasi dengan GPT
    while user_input != "bye":
        ask_gpt(user_input, chat_history, SYSTEM_MESSAGE)
        user_input = input("\nYou : ")

    # keluar dari gpt
    bye = "Bye, Dont forget to talk to me again (๑>ᴗ<๑)"
    print("\nGpt : ", end='')
    for char in bye:
        print(char, end='',flush=True)
        time.sleep(0.05)

# gpt API dan Response
def ask_gpt(prompt: str, chat_history: list, system_message: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    user_prompt = {"role": "user", "content": prompt}
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            *chat_history,
            user_prompt,
        ],
    )

    content = response["choices"][0]["message"]["content"]
    chat_history.append(user_prompt)
    chat_history.append({"role": "assistant", "content": content})

    # Print respon gpt huruf per huruf
    print("\nGpt : ", end='')
    for char in content:
        print(char, flush=True ,end='')
        time.sleep(0.05)
    print()
    return content


if __name__ == "__main__":
    main()
