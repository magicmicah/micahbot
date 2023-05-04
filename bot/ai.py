import settings
import openai
import nltk
import replicate
import tiktoken
import logging

logger = logging.getLogger(__name__)

# download necessary data and packages
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


## OpenAI Stuff

def get_openai_completion(prompt, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, stop):
    openai.api_key = settings.OPENAI_API_KEY
    try:
        response = openai.Completion.create(prompt=prompt, model=model, temperature=temperature, max_tokens=max_tokens, top_p=top_p, frequency_penalty=frequency_penalty, presence_penalty=presence_penalty, stop=stop)
        return response.choices[0].text
    except openai.error.APIConnectionError:
        return "I'm having trouble connecting to the internet right now. Try again later."

## OpenAI Chatbot

async def get_openai_chat_completion(model, messages, user, max_tokens=100):
    openai.api_key = settings.OPENAI_API_KEY

    try:
        response = openai.ChatCompletion.create(model=model, messages=messages, user=user, max_tokens=max_tokens)
        return response['choices'][0]['message']['content']
    except openai.error.APIConnectionError:
        logger.info("API Connection Error")
        return "I'm having trouble connecting to the internet right now. Try again later."


def num_characters_from_messages(messages):
    content_length_sum = 0
    for item in messages:
        content_length_sum += len(item['content'])
    return content_length_sum

## NLTK Stuff
## Find the nouns in a sentence
def get_nouns(sentence):
    tokens = word_tokenize(sentence)
    tokens = [token for token in tokens if token.lower() not in stopwords.words('english')]
    pos_tags = nltk.pos_tag(tokens)
    nouns = [word for word, pos in pos_tags if pos.startswith('N')]

    return nouns


## Replicate Stuff

async def get_replicate_image(prompt, negative_prompt=None):

    model = "stability-ai/stable-diffusion"
    version = "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf"
    model_version = (f"{model}:{version}")

    if negative_prompt is None:
        negative_prompt = ""
    image = replicate.run(
        model_version,
        input={
            "prompt": prompt,
            "negative_prompt": negative_prompt,
        }
    )
    return image[0]

def check_pc_language(message):
    if ("hey guys" in message.content.lower() or 'you guys' in message.content.lower()):
        return "Using 'guys' is not a gender inclusive greeting. Please use 'Hey everyone' or 'Hey all' instead. Thanks!"
    

