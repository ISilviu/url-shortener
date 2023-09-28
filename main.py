from fastapi import FastAPI
from pydantic import BaseModel
import random
import string


app = FastAPI()
random.seed(10)
shortened_urls = {}


class Url(BaseModel):
    url: str


def generate_random_url():
    return random.choice(string.ascii_lowercase)


def generate_url():
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=6))
    shortened_url = f'http://localhost:/8000/{random_letters}'
    return shortened_url


@app.post("/")
def shorten_url(url: Url):
    shortened_url = generate_url()
    while shortened_url in shortened_urls:
        shortened_url = generate_url()

    shortened_urls[shortened_url] = url
    return shortened_url
