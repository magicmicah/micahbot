from dotenv import load_dotenv
import requests
import settings


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

def report_message():
    return "We believe in freedom of speech around these parts. Take it up with the person you're reporting."