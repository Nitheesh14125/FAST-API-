from fastapi import FastAPI 

app = FastAPI()

@app.get('/sample')
def index():
    return 'Hey hi'

@app.get('/') #returing a json api 
def json():
    return {"data": {"name": "Nitheesh"}}


@app.get('/about')
def about():
    return {
        "data":{
            "name":"S.Nitheesh",
            "age":19,
            "Gender":"Male",
            "Profession":"Student"
        }
    }