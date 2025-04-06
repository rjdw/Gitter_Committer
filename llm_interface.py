import openai
import os
from string import Template

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_prompt_template(path="prompts/summary.txt"):
    with open(path, "r") as f:
        return Template(f.read())

def summarize_diff(diff_text):
    template = load_prompt_template()
    filled_prompt = template.substitute(git_diff=diff_text)

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a software engineer skilled in code reviews."},
            {"role": "user", "content": filled_prompt}
        ],
        temperature=0.2
    )
    return response['choices'][0]['message']['content']
