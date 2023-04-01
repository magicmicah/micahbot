import settings
import openai
import nltk

# download necessary data and packages
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



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

## Find the nouns in a sentence
def get_nouns(sentence):
    tokens = word_tokenize(sentence)
    tokens = [token for token in tokens if token.lower() not in stopwords.words('english')]
    pos_tags = nltk.pos_tag(tokens)
    nouns = [word for word, pos in pos_tags if pos.startswith('N')]

    return nouns