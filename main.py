from fastapi import FastAPI 

app = FastAPI()

@app.get('/sample')
def index():
    return 'Hey hi'


