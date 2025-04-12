import openai
import os
from string import Template
from google import genai
from importlib.resources import files
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GENAI_API_KEY") # https://aistudio.google.com/apikey

def load_prompt_template(path = "basic_PR_template.txt"):
    prompt_path = files("gittercommitter.prompts").joinpath(path)
    with prompt_path.open("r") as f:
        return Template(f.read())

def summarize_diff_openai(diff_text):
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

def summarize_diff_gemini(diff_text, file_data_formatted):
    template = load_prompt_template("pull_summary.txt")   
    filled_prompt = template.substitute(
        git_diff=diff_text,
        file_data_formatted=file_data_formatted
    )
    client = genai.Client(api_key=GEMINI_API_KEY)

    content = [filled_prompt]
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=content
    )
    # print(response.__dict__.keys())
    return response.text

def generate_commit_message_gemini(diff_text, file_data_formatted):
    template = load_prompt_template("commit_message_prompt.txt")   
    filled_prompt = template.substitute(
        git_diff=diff_text,
        file_data_formatted=file_data_formatted
    )
    client = genai.Client(api_key=GEMINI_API_KEY)

    content = [filled_prompt]
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=content
    )
    # print(response.__dict__.keys())
    return response.text