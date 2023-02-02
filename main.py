from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def index():
    return {'data':{'name': 'Jova'}}

@app.get('/about')
def about():
    return "textAbout"