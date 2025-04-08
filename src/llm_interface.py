import openai
import os
from string import Template
from google import genai

openai.api_key = os.getenv("OPENAI_API_KEY")
# dont forget to remove keys when pushing
GEMINI_API_KEY = "" # https://aistudio.google.com/apikey

def load_prompt_template(path="prompts/summary.txt"):
    with open(path, "r") as f:
        return Template(f.read())

def summarize_diff(diff_text):
    template = load_prompt_template()
    filled_prompt = template.substitute(git_diff=diff_text)

    # don't run this shit - take it out and add llama for free
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a software engineer skilled in code reviews."},
            {"role": "user", "content": filled_prompt}
        ],
        temperature=0.2
    )
    return response['choices'][0]['message']['content']

def summarize_diff_gemini(diff_text):
    template = load_prompt_template()
    filled_prompt = template.substitute(git_diff=diff_text)    

    client = genai.Client(api_key=GEMINI_API_KEY)

    content = [filled_prompt, "Summarize this"]
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=content
    )
    print(response.text)

