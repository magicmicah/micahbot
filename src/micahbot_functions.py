from dotenv import load_dotenv
import requests
import settings
import openai

def get_dadjoke():
    url = settings.DADJOKE_URL

    headers = {
        'x-rapidapi-key': settings.RAPID_API_KEY,
    }
    params = {

    }

    response = requests.request("GET", url, headers=headers, params=params)

    joke = response.json()

    joke_setup = joke['body'][0]['setup']
    joke_punchline = joke['body'][0]['punchline']
    joke_message = f"Here's a bad one. {joke_setup}...{joke_punchline}"

    return(joke_message)

def get_startup_idea():

    url = settings.STARTUP_IDEA_URL
    response = requests.get(url)
    idea = response.json()
    this = idea['this']
    that = idea['that']
    startup_idea = f"Here's your next startup idea. It's a {this} for {that}"
    return startup_idea

def get_openai_completion(prompt, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, stop):
    openai.api_key = settings.OPENAI_API_KEY
    try:
        response = openai.Completion.create(prompt=prompt, model=model, temperature=temperature, max_tokens=max_tokens, top_p=top_p, frequency_penalty=frequency_penalty, presence_penalty=presence_penalty, stop=stop)
        return response.choices[0].text
    except openai.error.APIConnectionError:
        return "I'm having trouble connecting to the internet right now. Try again later."