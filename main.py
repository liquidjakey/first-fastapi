from fastapi import FastAPI, Request
import random
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/lunch")
def lunch():
    menu =['Pizza', 'Burger', 'Salad', 'Pasta']
    return {
        'pick': random.choice(menu)
    }

@app.get("/lotto")
def lotto():
    numbers = random.sample(range(1, 46), 6)
    return {
        'numbers': numbers
    }

@app.get('/lotto/html')
def lotto_html(request: Request):
    numbers = sorted(random.sample(range(1, 46), 6))
    return templates.TemplateResponse(
        request=request,
        name='lotto.html',
        context={'numbers': numbers, 'hi':'Jacob'}
        )

@app.get('/profile')
def profile(username:str):
    return {'username': username}

@app.get('/cube/{number}')
def cube(number:int):
    return {'number': number ** 3}

@app.get('/add/lotto')
def lotto_api(count:int = 1):
    games = []
    for _ in range(count):
        numbers = sorted(random.sample(range(1, 46), 6))
        games.append(numbers)
    return {'result': games}

@app.get('/add/lotto/html2')
def lotto_html2(request):
    games = [random.sample(range(1, 46), 6) for _ in range(5)]
    return templates.TemplateResponse(
        request=request,
        name='lotto2.html',
        context={'games': games}
        )

@app.get('/ping')
def ping(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='ping.html')

@app.get('/pong')
def lotto_pong(request: Request, count:int):
    games = [random.sample(range(1, 46), 6) for _ in range(count)]
    return templates.TemplateResponse(
        request=request,
        name='lotto2.html',
        context={'games': games}
        )
