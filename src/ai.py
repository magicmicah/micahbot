import settings
import openai
import nltk
import replicate

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

def get_openai_chat_completion(model, messages, user):
    openai.api_key = settings.OPENAI_API_KEY
    try:
        response = openai.ChatCompletion.create(model=model, messages=messages, user=user)
        return response['choices'][0]['message']['content']
    except openai.error.APIConnectionError:
        return "I'm having trouble connecting to the internet right now. Try again later."


## NLTK Stuff
## Find the nouns in a sentence
def get_nouns(sentence):
    tokens = word_tokenize(sentence)
    tokens = [token for token in tokens if token.lower() not in stopwords.words('english')]
    pos_tags = nltk.pos_tag(tokens)
    nouns = [word for word, pos in pos_tags if pos.startswith('N')]

    return nouns


## Replicate Stuff

def get_replicate_image(prompt):

    model = "stability-ai/stable-diffusion"
    version = "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf"
    model_version = (f"{model}:{version}")

    image = replicate.run(
        model_version,
        input={"prompt": prompt}
    )
    return image[0]


