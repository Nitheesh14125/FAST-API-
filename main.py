from fastapi import FastAPI 

app = FastAPI()


@app.get('/sample')
def sample():
    return 99

@app.get('/samplestring')
def samplestring():
    return "Sample string returing"

@app.get('/jsondata')
def json_data():
    return {
        "Name":"Nitheesh",
        "Age": 19,
        "Gender":"Male",
        "Profession":"Student"
    }


@app.get('/')
def index():
    return {
        "Type this below URL to go there pages":"Values",
        "URL_sample":"/sample",
        "URL_samplestring":"/samplestring",
        "URL_jsondata":"/jsondata",
        "URL_Pass_Parameter":r"/items/{there_id}"
    }

#pass parameters
@app.get("/items/{item_id}")
def item_value(item_id):
    return {
        "Item id":item_id
    }

