
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

# model = "text-davinci-003"

# prompt = "What is the meaning of life?"
# response = openai.Completion.create(model=model, prompt=prompt, max_tokens=100, temperature=0.5, top_p=1, frequency_penalty=0.0)
# print(response.choices)


model = "code-davinci-002"

code = "class Log:\
    def __init__(self, name): \
        self.name = name\
    def delete(self):\
        print(f\"Deleting {self.name}\")"


prompt = code + "\n" + "\"\"\"" + "Summarize the above code for me: \n"
response = openai.Completion.create(
  model="code-davinci-002",
  prompt=prompt,
  temperature=0,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\"\"\""]
)

print(response.choices)