from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import random
import string


app = FastAPI()
random.seed(10)
url_codes = {}


class Url(BaseModel):
    url: str


def generate_random_url():
    return random.choice(string.ascii_lowercase)


def generate_random_letters():
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=6))
    return random_letters


@app.post("/")
def shorten_url(url: Url):
    random_letters = generate_random_letters()
    while random_letters in url_codes:
        random_letters = generate_random_letters()

    url_codes[random_letters] = url
    shortened_url = f'http://localhost:8000/{random_letters}'
    return shortened_url


@app.get("/{route_code}")
def re_route(route_code):
    original_url = url_codes.get(route_code)
    if original_url:
        print(original_url)
        return RedirectResponse(url=original_url.url)
